Dataset **EndoNuke** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](/supervisely-supervisely-assets-public/teams_storage/I/F/Bu/bKt9664olC5PJXzc9DYfARAWwkhDki1pZYMijWyY23a67QbsjYF7sYxcNqCsFZ0Ujz8wtberQprgeDPA9uQnycnu77joJsXO6GKheG9N0rhP8YsnhTrWS9Hh1rbj.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='EndoNuke', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.ispras.ru/conf/endonuke/data.zip).