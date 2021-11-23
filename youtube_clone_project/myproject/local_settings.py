SECRET_KEY = 'a!jn2bomp2enq7!%u!law)l0s%pk0g8mk6*580uw7+%*ka5@7b'



DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone',
        'USER': 'root',
        'PASSWORD': '2Bearcats',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }

    }
}