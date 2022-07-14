def AWSGlueCatalogBackend(**kwargs):
    """
    AWS Glue Catalog Backend
    """
    from .aws_glue_catalog import AWSGlueCatalog
    return AWSGlueCatalog(**kwargs)