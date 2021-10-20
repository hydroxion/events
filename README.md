# Events

Schedule events over time.

## About

Schedule events over time with Redis pub / sub.

## Built with

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Redis](https://redis.io/)
- [Schedule](https://schedule.readthedocs.io/en/stable/)
- [Docker](https://www.docker.com/)

## Installation

Use the package manager APT to install Docker and Docker Compose.

```sh
apt install docker.io
```

```sh
curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

mv /usr/local/bin/docker-compose /usr/bin/docker-compose

chmod +x /usr/bin/docker-compose
```

Download the necessary Docker images and create an API container.

```sh
docker-compose -f docker-compose.yml up -d
```

## Usage

When an API container is created the API is already available at [0.0.0.0:5000](http://0.0.0.0:5000/).

Check the documentation below to use the available endpoints.

## Documentation

Use the [Insomnia](https://insomnia.rest/) HTTP client to load the [events](./insomnia.json) playground and read the documentation for each endpoint.

## Contributing

Pull requests are welcome. Please, consider the following.

1. Make sure you code have quality, a.k.a standards
2. Make sure your code is secure
3. Make sure your code has no performance issues
4. Make sure your code is documented, if necessary
5. Describe the changes that were done

> No issue or PR template required, but be informative

## License

[MIT](./LICENSE.md)
