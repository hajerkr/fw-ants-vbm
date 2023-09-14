import subprocess

def MNI2BCP(BCP, OUTPUT_DIR):
    MNI = '/flywheel/v0/app/templates/MNI152_T1_1mm_brain.nii.gz'
    OUT = (OUTPUT_DIR + '/mniTobcp_')

    print('BCP: ' + BCP)
    print('MNI: ' + MNI)
    print('OUT: ' + OUT)
    subprocess.run(['antsRegistrationSyNQuick.sh -f ' + BCP + ' -m ' + MNI + ' -t s -o ' + OUT], shell=True, check=True)

