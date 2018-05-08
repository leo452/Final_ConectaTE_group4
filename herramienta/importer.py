# -*- coding: utf-8 -*-
from cuser.middleware import CuserMiddleware
from data_importer.core.base import reduce_list
from data_importer.core.exceptions import StopImporter
from data_importer.importers import CSVImporter
import models
from django.core.cache import cache

class CSVImporterTool(CSVImporter):
    fields = ['nombre', 'descripcion', 'licencia', 'enlaces', 'descarga_url', 'sistema_operativo', 'version', 'documentacion']
    data_tem =None

    def __init__(self, source=None, id_file=0, *args, **kwargs):
        self.id_file =id_file
        super(CSVImporterTool, self).__init__(source=source, *args, **kwargs)

    class Meta:
        model = models.Herramienta
        delimiter = ','
        ignore_first_line = False

    def validar_columnas(self):
        if hasattr(self._reader, 'read'):
            reader = self._reader.read()
        else:
            reader = self._reader
        self.data_tem = reader
        for row, values in enumerate(self.data_tem, 1):
            if row==1:
                if len(values) == len(self.fields):
                    return True
                else:
                    return False

    def save(self, instance=None):
        list_data = []
        for row, values in self.cleaned_data:
            resp={'row': row}
            if values['nombre'] != '':
                for key, value in values.items():
                    resp.update({key: value})
            else:
                resp.update({'nombre': 'Debe registrar un nombre'})
            list_data.append(resp)
        return list_data

    def process_row(self, row, values):
        """
        Read clean functions from importer and return tupla with row number, field and value
        """
        values_encoded = [self.to_unicode(i) for i in values]
        try:
            # reduce list
            if self._reduce_list:
                values_encoded = reduce_list(self._reduce_list, values_encoded)
            values = dict(zip(self.fields, values_encoded))
        except TypeError:
            raise TypeError('Invalid Line: {0!s}'.format(row))


        # validate full row data
        try:
            values = self.clean_row(values)
        except Exception as e:
            self._error.append(self.get_error_message(e, row))
            return None
        return (row, values)
