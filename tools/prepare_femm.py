"""Prepare a separate FEMM run folder without overwriting source data."""
from pathlib import Path
import argparse
import re
import shutil
ROOT=Path(__file__).resolve().parents[1]

def prepare(output):
    output=Path(output).resolve()
    protected=[ROOT/'cad',ROOT/'simulation',ROOT/'archive']
    if any(output==p or p in output.parents for p in protected):
        raise ValueError('Run output must be outside preserved source directories')
    if output.exists():
        raise FileExistsError('Choose a new run directory; existing runs are preserved')
    if '"' in output.as_posix() or '\n' in output.as_posix():
        raise ValueError('Output path cannot be represented safely in Lua')
    source=ROOT/'simulation/rev64'
    script=(source/'Rev64_sweep_and_validate.lua').read_text(encoding='utf-8')
    prefix=output.as_posix()+'/'
    for key in ['BASE_DIR','WORK_DIR']:
        script,count=re.subn(r'^'+key+r' = .*$',lambda m:key+' = "'+prefix+'"',script,flags=re.M)
        if count!=1: raise ValueError(f'Expected one {key} assignment')
    script=re.sub(r'^quit\(\)\s*$', '-- Keep FEMM open after this isolated run.',script,flags=re.M)
    output.mkdir(parents=True)
    shutil.copy2(source/'Rev64_CENTERED_0p5mm_BOBBIN_80T.fem',output)
    (output/'run_sweep.lua').write_text(script,encoding='utf-8')
    return output

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    print('Prepared isolated FEMM inputs:',prepare(args.output))
