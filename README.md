# OctoSCAD

Octo - as it's multicore
SCAD - um... because it's for openSCAD...

## About

Export from openSCAD in bulk, using combinations of parameters

## Usage

[To be determined]
```bash
octoscad configurationFile.json

#alternatively
octoscad {jsonContent}
```


```json
{
  filename.scad:[
    {
      "width": [10,90,37,53],
      "height": 33,
      "depth": {
        from: 3
        to: 8
        step: 2
      },
      "textParam": ["hello","world"]
    }
  ],
  filename2.scad:[
  ...
  ]
}
```


