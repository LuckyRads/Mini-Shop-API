class DBConfig:
    hostname = '127.0.0.1'
    port = 3306
    username = 'root'
    password = 'root'
    database = 'shop'

    @staticmethod
    def get_mysql_config_string():
        return f'mysql://{DBConfig.username}:{DBConfig.password}@{DBConfig.hostname}:{DBConfig.port}/{DBConfig.database}'
