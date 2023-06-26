Dataset **ENDONUKE** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/v/U/jl/tjYhswti2vTD3TLfSpfOrl4RvKO6FjMcjlUiWbHoyqkvrqM3nFb0U8uBCmkiSjbhrQLGS56mNXL8roz3uC3rlWWrIbfLyScwy6Ykf84MhpVMFiG7PiNQrNf55EWP.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='ENDONUKE', dst_path='~/dtools/datasets/ENDONUKE.tar')
```
The data in original format can be 🔗[downloaded here](https://www.ispras.ru/conf/endonuke/data.zip)