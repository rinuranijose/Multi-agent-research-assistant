@echo off
echo Starting Multi-Agent Assistant...

REM Start Redis
start cmd /k "cd /d C:\Users\USER && redis-server"

REM Start Ollama
start cmd /k "ollama run phi3"

REM Start MCP Server
start cmd /k "cd /d %cd% && python mcp_server\server.py"

REM Start Django Backend
start cmd /k "cd /d %cd%\backend && python manage.py runserver"

REM Start Streamlit UI
start cmd /k "cd /d %cd% && streamlit run streamlit_app\app.py"

echo All services are starting...
pause