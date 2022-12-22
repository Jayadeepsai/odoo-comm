{
    'name':'School',
    'version':'1.1',
    'author':'Deepu',
    'summary':'School Management System',
    'description':"""School Management""",
    'category':'School',
    'depends':['base'],
    'data':[
        "security/ir.model.access.csv",
        "views/school_view.xml"
    ],

    'application' : True,
    'installable': True,

}