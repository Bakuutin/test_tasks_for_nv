import csv

from django.views.generic import View
from django.http import StreamingHttpResponse
from django.db import connection


def customers_iterator(array_size=1000):
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT
               nv_customer.id,
               nv_customer.first_name,
               nv_customer.last_name,
               nv_email.address,
               nv_phone.number
            FROM nv_customer
            LEFT OUTER JOIN nv_email ON nv_customer.id = nv_email.customer_id
            LEFT OUTER JOIN nv_phone ON nv_customer.id = nv_phone.customer_id
            '''
        )
        while True:
            results = cursor.fetchmany(array_size)
            if not results:
                break
            for result in results:
                yield result


class Buffer(object):
    def write(self, value):
        return value


class ExportView(View):
    def get(self, request):
        writer = csv.writer(Buffer())
        response = StreamingHttpResponse(
            streaming_content=(writer.writerow(row) for row in customers_iterator()),
            content_type='text/csv'
        )
        response['Content-Disposition'] = 'attachment; filename="customers.csv"'
        return response
