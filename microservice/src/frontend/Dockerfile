# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# 使用 .NET SDK 镜像作为构建环境
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS builder

# 安装 Go 工具链
RUN apt-get update && apt-get install -y wget && \
    wget -q https://go.dev/dl/go1.23.0.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.23.0.linux-amd64.tar.gz && \
    rm go1.23.0.linux-amd64.tar.gz

# 设置 Go 环境变量 - 必须在同一 RUN 命令中安装后立即设置
ENV PATH="/usr/local/go/bin:${PATH}" \
    GOROOT="/usr/local/go" \
    GOPATH="/go"


# 设置工作目录
WORKDIR /src

# 恢复依赖项
COPY go.mod go.sum ./
RUN go mod download

# 复制源代码
COPY . .

# Skaffold 传递调试编译标志
ARG SKAFFOLD_GO_GCFLAGS

# 构建应用（静态编译）
RUN CGO_ENABLED=0 GOOS=linux go build \
    -gcflags="${SKAFFOLD_GO_GCFLAGS}" \
    -o /app/frontend .

# 运行时阶段 - 使用轻量级基础镜像
FROM mcr.microsoft.com/dotnet/runtime-deps:8.0-jammy-chiseled
WORKDIR /app

# 从构建阶段复制二进制文件
COPY --from=builder /app/frontend .

# 复制静态资源
COPY --from=builder /src/templates ./templates
COPY --from=builder /src/static ./static

# 用于调试的环境变量
# 默认行为 - 失败时打印当前 goroutine 的堆栈跟踪
ENV GOTRACEBACK=single

# 暴露端口
EXPOSE 8080

# 入口点
ENTRYPOINT ["/app/frontend"]