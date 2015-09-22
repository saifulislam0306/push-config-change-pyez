
from jnpr.junos import Device
from jinja2 import Template
import yaml
import sys
from glob import glob
dev = Device('192.168.0.1')
from jnpr.junos.utils.config import Config
cu = Config(dev)
dev.open()
# YAML file.
with open(glob('datavars.yml')[0]) as fh:
    data = yaml.load(fh.read())

# Jinja2 template file.
with open(glob('config-example-template.conf')[0]) as t_fh:
    t_format = t_fh.read()

template = Template(t_format)
print (template.render(data))

rsp = cu.load( template_path="config-example-template.conf", template_vars=data )
cu.commit()