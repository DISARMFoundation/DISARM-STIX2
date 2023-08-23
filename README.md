# DISARM STIX2 Generator

## Install

```shell
# get code
git clone https://github.com/DISARMFoundation/DISARM-STIX2
cd DISARM-STIX2
# create venv
python3 -m venv DISARM-STIX2_venv
source DISARM-STIX2_venv/bin/activate
# install requirements
pip3 install -r requirements.txt
# download the latest version of the DISARM Framework xlsx
curl https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/DISARM_MASTER_DATA/DISARM_FRAMEWORKS_MASTER.xlsx > DISARM_FRAMEWORKS_MASTER.xlsx
```

## Run

```shell
# generate STIX objects in the output/ folder
python3 main.py
```

## DISARM STIX2

The DISARM STIX2 Generator encodes the DISARM object into the corresponding STIX2 object shown in the following table.

| DISARM    | STIX2                 |
|-----------|-----------------------|
| Matrix    | Matrix (MITRE custom) |
| Tactic    | Tactic (MITRE custom) |
| Technique | AttackPattern         |

## MITRE ATT&CK Navigator

DISARM STIX is compatible with the MITRE ATT&CK Navigator.

DISARM object types, such as `Matrix`, `Tatic` are prefixed with `x-mitre--` for compatibility reasons.

DISARM `AttackPattern` objects also contain `x_mitre_is_subtechnique` and `x_mitre_platforms` properties for compatability.  These properties cannot be removed without upstream changes to the ATT&CK Navigator.

## OpenCTI

DISARM STIX can be imported into OpenCTI via the OpenCTI STIX Importer plugin which is installed in OpenCTI by default.
Alternatively, use the OpenCTI DISARM plugin to continuously pull the latest DISARM STIX.

