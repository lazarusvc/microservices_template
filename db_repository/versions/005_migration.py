from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
api = Table('api', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('status', String(length=512)),
    Column('meta_data', String(length=512)),
    Column('data', String(length=512)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['api'].columns['meta_data'].create()
    post_meta.tables['api'].columns['status'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['api'].columns['meta_data'].drop()
    post_meta.tables['api'].columns['status'].drop()
