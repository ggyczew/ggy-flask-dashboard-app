#!/bin/bash

flask db init;
flask db migrate;
flask db upgrade;
# flask commands init_users;
# flask commands init_sample_data;