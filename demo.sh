#!/bin/bash
# JetBot Upgraded – one-command demo launcher for indie makers

set -e
cd "$(dirname "$0")"

show_help() {
  cat << EOF
JetBot Upgraded – Demo Launcher

Usage:
  ./demo.sh <command> [options]

Cool demos:
  follow [args]     YOLO object following
  find [args]       Search + approach an object
  wander            Smart autonomous wander
  voice             Voice commands (or --keyboard)
  dashboard         Web control from your phone

Build & understand:
  build             Interactive build assistant
                    (what you have → how to assemble)

Examples:
  ./demo.sh follow
  ./demo.sh find --target cup
  ./demo.sh dashboard
  ./demo.sh build

Docs:
  docs/build/INTERACTIVE_BUILD_GUIDE.md   ← start here for assembly
  docs/build/VIDEO_RESOURCES.md          ← YouTube videos for every concept
  docs/build/COMPONENT_MAP.md
  docs/designs/JETNOVA.md
  docs/INDIE_GUIDE.md
  docs/COOL_DEMOS.md
  docs/STUDENTS_AND_EDUCATORS.md     ← learning path for classes
EOF
}

case "${1:-}" in
  follow|yolo)
    shift
    echo "→ YOLO Object Following"
    python3 demos/yolo_follow.py "$@"
    ;;
  find|search)
    shift
    echo "→ Find Object"
    python3 demos/find_object.py "$@"
    ;;
  wander|explore)
    shift
    echo "→ Smart Wander"
    python3 demos/smart_wander.py "$@"
    ;;
  voice)
    shift
    echo "→ Voice Control"
    python3 demos/voice_control.py "$@"
    ;;
  dashboard|web)
    shift
    IP=$(hostname -I 2>/dev/null | awk '{print $1}')
    echo "→ Web Dashboard"
    echo "  Open  http://${IP:-<jetson-ip>}:8080  on your phone"
    python3 demos/web_dashboard.py "$@"
    ;;
  build|assistant)
    echo "→ Interactive Build Assistant"
    python3 tools/build_assistant.py
    ;;
  help|-h|--help|"")
    show_help
    ;;
  *)
    echo "Unknown command: $1"
    echo
    show_help
    exit 1
    ;;
esac
