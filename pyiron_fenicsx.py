__version__ = "0.1"
__all__ = []


from pyiron_base import JOB_CLASS_DICT

from pyiron_base import Project as ProjectBase

# Make classes available for new pyiron version
JOB_CLASS_DICT['Fenicsx'] = 'mod_pyiron_continuum.fenicsx.job.generic'
