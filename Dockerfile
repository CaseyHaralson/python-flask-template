FROM mambaorg/micromamba:1.5.6
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -n base -f /tmp/environment.yml && \
    micromamba clean --all --yes
ARG MAMBA_DOCKERFILE_ACTIVATE=1  # (otherwise python will not be found)
RUN micromamba install gunicorn -c conda-forge && \
    micromamba clean --all --yes

USER $MAMBA_USER
COPY --chown=$MAMBA_USER:$MAMBA_USER . /project/
WORKDIR /project

# https://stackoverflow.com/a/64898830/2155085
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

# todo: https://uwekorn.com/2021/03/01/deploying-conda-environments-in-docker-how-to-do-it-right.html
