def createTaskTemp(name,status,type):
    temp=f"""
    <task>
        <name>{name}</name>
        <status>{status}</status>
        <type>{type}</type>
    </task>
    """

    return temp