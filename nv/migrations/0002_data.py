from django.db import migrations


def inform(text):
    return migrations.RunPython(
        lambda apps, schema_editor: print('\n  {}'.format(text), end=''),
        migrations.RunPython.noop
    )


class Migration(migrations.Migration):

    dependencies = [
        ('nv', '0001_initial'),
    ]

    operations = [
        inform('Please, wait a bit...'),
        migrations.RunSQL(
            """
            CREATE PROCEDURAL LANGUAGE 'plpython3u' HANDLER plpython_call_handler;

            CREATE OR REPLACE FUNCTION create_customers() RETURNS boolean AS
            $$
                import plpy
                from itertools import product

                names = ['Mary', 'Jane', 'Peter', 'Saya', 'Max']
                surnames = ['Red', 'Green', 'Black', 'Blue', 'White']
                values_string = str(tuple(product(names, surnames)))[1:-1]
                try:
                    for i in range(2000000 // 25): # divide by number of values pairs
                        plpy.execute("INSERT INTO nv_customer(first_name, last_name) VALUES {}".format(values_string))
                except plpy.SPIError:
                    return False
                return True
            $$
            LANGUAGE 'plpython3u' VOLATILE;
            SELECT create_customers();
            """,
            reverse_sql='',
        ),
        inform('Customers created, creating emails and phones...'),
        migrations.RunSQL(
            """
            CREATE OR REPLACE FUNCTION create_emails_and_phones() RETURNS boolean AS
            $$
                import plpy
                from random import randint

                cursor = plpy.cursor("SELECT id from nv_customer")
                try:
                    while True:
                        rows = list(cursor.fetch(1000))
                        if not rows:
                            break

                        customer_ids = [row['id'] for row in rows + rows[:randint(2, 30)]]

                        plpy.execute("INSERT INTO nv_phone(number, customer_id) VALUES {}".format(str(tuple(
                            (
                                '+{}{}000000'.format(customer_id, i % 13)[:10],
                                customer_id,
                            ) for i, customer_id in enumerate(customer_ids)
                        ))[1:-1]))

                        plpy.execute("INSERT INTO nv_email(address, customer_id) VALUES {}".format(str(tuple(
                            (
                                '{}{}@example.com'.format(customer_id, i % 13)[-31:],
                                customer_id,
                            ) for i, customer_id in enumerate(customer_ids)
                        ))[1:-1]))
                except plpy.SPIError:
                    return False
                return True
            $$
            LANGUAGE 'plpython3u' VOLATILE;
            SELECT create_emails_and_phones();
            """,
            reverse_sql='',
        ),
    ]
