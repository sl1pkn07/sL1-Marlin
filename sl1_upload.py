Import("env")
env.AlwaysBuild(env.Alias("push", "$BUILD_DIR/${PROGNAME}.bin", ["curl --retry 5 -T $SOURCES $UPLOAD_PORT > /dev/null && echo 'Upload Done'"]))
