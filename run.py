import os

from app import create_app

if __name__ == '__main__':
    env_name = 'development'
    app = create_app(env_name)

    # run app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
