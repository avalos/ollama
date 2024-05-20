# https://github.com/ollama/ollama/blob/main/docs/api.md
FROM ollama/ollama:0.1.38
#ENV LLM=dolphin-phi
ARG LLM
ENV LLM=${LLM}
EXPOSE 11434
RUN echo MODEL: "$LLM"
RUN ollama serve & sleep 5 ; ollama pull "$LLM"
ENTRYPOINT ["ollama"]
CMD ["serve"]
