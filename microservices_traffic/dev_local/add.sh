#!/bin/bash

krabbitmqctl add_user test test -s rabbitmq-app -c rabbitmq-app
krabbitmqctl set_user_tags test administrator -s rabbitmq-app -c rabbitmq-app
krabbitmqctl set_permissions -p / test ".*" ".*" ".*" -s rabbitmq-app -c rabbitmq-app


#rabbitmqctl add_user test test && rabbitmqctl set_user_tags test administrator && rabbitmqctl set_permissions -p / test ".*" ".*" ".*"

