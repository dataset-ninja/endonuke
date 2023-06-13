Dataset **ENDONUKE** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/N/h/yh/4nlfH5LCK3yH5CzVLRM3nTUUln2iAv1vPIbhUYbS5rqWwG6ZB0QINPSSBBVhYJlZgJLnesRWgUabQ9dSzGmLi5oQw4AFilKDlDSP9BbzBm0yQvOGe3BgEiilRM7P.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='ENDONUKE', dst_path='~/dtools/datasets/ENDONUKE.tar')
```
The data in original format can be 🔗[downloaded here.](https://www.ispras.ru/conf/endonuke/data.zip)