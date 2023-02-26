mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $POST\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml