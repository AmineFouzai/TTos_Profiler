# TTos_Profiler
on windows:
was on conda 4.8.3, open Anaconda Prompt
```
conda update ipykernel
conda update --all
```
repeat the above update till no error (took few runs for me), then run:

```
conda create -n face_recognition python==3.6.6 
conda activate face_recognition
```

``` pip install cmake
    pip install dlib==19.8.1
    pip install face_recognition
    pip install opencv-contrib-python==4.1.0.25
    pip install twisted 
  ```

----------------------------------------------------------- 

conda list 

```
# packages in environment at C:\user\user\Anaconda3\envs\face_recognition:
#
# Name                    Version                   Build  Channel
certifi                   2020.4.5.1               py36_0
click                     7.1.2                    pypi_0    pypi
cmake                     3.17.3                   pypi_0    pypi
dlib                      19.8.1                   pypi_0    pypi
face-recognition          1.3.0                    pypi_0    pypi
face-recognition-models   0.3.0                    pypi_0    pypi
numpy                     1.18.5                   pypi_0    pypi
opencv-contrib-python     4.1.0.25                 pypi_0    pypi
pillow                    7.1.2                    pypi_0    pypi
pip                       20.0.2                   py36_3
python                    3.6.6                hea74fb7_0
setuptools                47.1.1                   py36_0
vc                        14.1                 h0510ff6_4
vs2015_runtime            14.16.27012          hf0eaf9b_2
wheel                     0.34.2                   py36_0
wincertstore              0.2              py36h7fe50ca_0
```
on linux/macos:

```
pip install requirements.txt
```
