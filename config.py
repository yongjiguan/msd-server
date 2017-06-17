import os
import socket
from collections import OrderedDict


class BaseConfig:
    DB_NAME = 'msdserver.sqlite'
    DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep + DB_NAME

    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % DB_PATH
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SIMULATION_ENGINE = 'gmx'

    JOB_MANAGER = 'local'
    NPROC_PER_JOB = 1



class ClusterConfig(BaseConfig):
    WORK_DIR = '/share/workspace/msdserver/MSDServer/'
    DFF_ROOT = '/share/apps/dff/msdserver'
    PACKMOL_BIN = '/share/apps/tools/packmol'
    LMP_BIN = '/share/apps/lammps/lmp-stable'
    GMX_BIN = '/share/apps/gromacs/2016.3-static-compatible/bin/gmx'

    JOB_MANAGER = 'torque'
    QUEUE_DICT = OrderedDict([('cpu, 8')])


class MacConfig(BaseConfig):
    WORK_DIR = '/tmp/MSDServer/'
    DFF_ROOT = '/Users/zheng/Projects/DFF/Developing'
    PACKMOL_BIN = '/Users/zheng/Projects/DFF/Developing/bin32m/Packmol/packmol.exe'
    LMP_BIN = '/Users/zheng/Projects/DFF/Developing/bin32m/Lammps/lammps'
    GMX_BIN = '/opt/gromacs/2016.3/gmx'


class XPSConfig(BaseConfig):
    WORK_DIR = 'D:/Download/Temp'
    DFF_ROOT = 'D:/Projects/DFF/Developing'
    PACKMOL_BIN = 'D:/Projects/DFF/Developing/bin32w/Packmol/packmol.exe'
    LMP_BIN = 'D:/Projects/DFF/Developing/bin32w/Lammps/lammps.exe'
    GMX_BIN = None


Config = ClusterConfig
if socket.gethostname() == 'cluster.hpc.org':
    Config = ClusterConfig
elif socket.gethostname() == 'z-Mac.local':
    Config = MacConfig
elif socket.gethostname() == 'z-XPS':
    Config = XPSConfig
else:
    raise Exception('MSDServer will not work on this machine')
