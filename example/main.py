from latex_storage import Storage

def dump_data(storage, filename):
    storage.put(M_load='valueA', N_min='valueB')
    storage.put(**dict(
        ('engine.%s' % key, value) for key, value in engine.items()
    ))
    
    storage.export(filename)

dump_data(Storage(), 'latex/work.json')