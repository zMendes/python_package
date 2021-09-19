#!/usr/bin/env python3
import dev_aberto
from babel.dates import format_datetime
from datetime import datetime
import gettext

if __name__ == '__main__':
    gettext.install('cli', localedir='locale') 
    date, name = dev_aberto.hello()
    print(_('Last commit sent on:'), str(format_datetime(datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ'))), _(' by'), name)
