# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""classe para catalogar erros do Firewall Mikrotik"""
from django.db import models


# MIKROTIKFIREWALLNAT %{SYSLOGTIMESTAMP:date} MikroTik %{DATA:LogPrefix} %{DATA:LogChain}: in:%{DATA:src_zone}
# out:%{DATA:dst_zone}, src-mac %{MAC}, proto %{DATA:proto}, %{IP:src_ip}:%{INT:src_port}->%{IP:dst_ip}:%{INT:dst_port},
# NAT \(%{IP:nat_osrc_ip}:%{INT:nat_osrc_port}->%{IP:nat_nsrc_ip}:%{INT:nat_nsrc_port}\)->%{IP:nat_dst_ip}:%{INT:nat_dstport},
#len %{INT:length}

# MIKROTIKFIREWALLNAT %{SYSLOGTIMESTAMP:date} MikroTik %{DATA:LogPrefix} %{DATA:LogChain}: in:%{DATA:src_zone}
# out:%{DATA:dst_zone}, proto %{DATA:proto}, %{IP:src_ip}:%{INT:src_port}->%{IP:dst_ip}:%{INT:dst_port},
# NAT %{IP:nat_osrc_ip}:%{INT:nat_osrc_port}->\(%{IP:nat_nsrc_ip}:%{INT:nat_nsrc_port}->%{IP:nat_dst_ip}:%{INT:nat_dstport}\),
#len %{INT:length}

#testando git 2

class Firewall(models.Model):
    """classe para armazenar trafego no firewall com NAT"""
    data = models.DateField()
    hora = models.TimeField()
    LogPrefix = models.CharField(max_length=50, null=True)
    src_zone = models.CharField(max_length=50, null=True)
    dst_zone = models.CharField(max_length=50, null=True)
    src_mac = models.CharField(max_length=50, null=True)
    proto = models.CharField(max_length=50, null=True)
    src_ip = models.CharField(max_length=50, null=True)
    src_port = models.CharField(max_length=50, null=True)
    dst_ip = models.CharField(max_length=50, null=True)
    dst_port = models.CharField(max_length=50, null=True)
    nat_osrc_ip = models.CharField(max_length=50, null=True)
    nat_osrc_port = models.CharField(max_length=50, null=True)
    nat_nsrc_ip = models.CharField(max_length=50, null=True)
    nat_nsrc_port = models.CharField(max_length=50, null=True)
    nat_dst_ip = models.CharField(max_length=50, null=True)
    nat_dst_port = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.data

# MIKROTIKLOGINOUT %{SYSLOGTIMESTAMP:date} MikroTik user %{WORD:user}
# logged (?:out|in) from %{IP:src_ip}
# via %{WORD:src_type}


class FirewallLogin(models.Model):
    """classe para armazenar login/logout"""
    data = models.DateField()
    hora = models.TimeField()
    user = models.CharField(max_length=50, null=True)
    logged = models.CharField(max_length=50, null=True)
    src_ip = models.CharField(max_length=50, null=True)
    src_type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.data

# MIKROTIKLOGINFAIL %{SYSLOGTIMESTAMP:date} MikroTik login failure for user %{WORD:user} from %{IP:src_ip}
#via %{WORD:src_type}


class FirewallLoginError(models.Model):
    """classe para BD armazenar erros de autenticacao login/senha"""
    data = models.DateField()
    hora = models.TimeField()
    user = models.CharField(max_length=50, null=True)
    src_ip = models.CharField(max_length=50, null=True)
    src_type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.data
