FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN rm -f /etc/apt/sources.list.d/yarn.list /etc/apt/sources.list.d/yarn.list.save \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        coreutils \
        curl \
        git \
        git-lfs \
        gh \
        golang-go \
        python3-venv \
        wget \
        # --- For Rendering Game Windows ---
        fluxbox \
        tigervnc-standalone-server \
        xvfb \
        x11vnc \
        websockify \
        novnc \
        libsdl2-dev \
        libsdl2-image-dev \
        libsdl2-mixer-dev \
    && rm -rf /var/lib/apt/lists/*

USER vscode

ENV HOME=/home/vscode
ENV PATH="${HOME}/.local/bin:${HOME}/go/bin:/bin:/usr/bin:/usr/sbin:/sbin:${PATH}"
ENV GOBIN="${HOME}/go/bin"

RUN mkdir -p "${HOME}/.local/bin" "${HOME}/go/bin" \
    && PATH="/bin:/usr/bin:/usr/sbin:/sbin:${PATH}" curl -sS https://webi.sh/golang | sh \
    && /bin/bash -lc 'go install github.com/bootdotdev/bootdev@latest' \
    && curl -LsSf https://astral.sh/uv/install.sh | sh