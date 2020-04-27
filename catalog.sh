#!/bin/bash
# set -eo pipefail
# IFS=$'\n\t'

catalog () {

   install () {
    pip3 install virtualenv
    if [ ! -d "./catalog-env" ]
    then
      virtualenv catalog-env
    fi
    source ./catalog-env/bin/activate
    pip3 install -r ./requirements.txt
    echo "Succesfuly instaled catalog in virtual env catalog-env. Run source ./catalog-env/bin/activate to switch catalog-env."
  }

  build () {
    docker build -t catalog .
  }

  run () {
    docker run -p 5005:5005 -it catalog
  }

  help () {
    cat <<-EOF
catalog commands:
  install            -> install catalog in a new python environment "catalog-env"
  build              -> build application
  run                -> run application
  help               -> display this message
EOF
  }


  case $1 in
    install)
      install $@
      ;;
    build)
      build $@
      ;;
    run)
      run $@
      ;;
    help)
      help $@
      ;;
    *)
      help $@
      ;;
  esac
}

catalog $@

