# %%
import requests
import json
import polars as pl
from youtube_transcript_api import YouTubeTranscriptApi
from sentence_transformers import SentenceTransformer
import os

def getVideoIDs():
    print('Step 0 hi')


def getVideoTranscripts():
    """
        Function to extract transcripts for all video IDs stored in "data/video-ids.parquet"

        Dependencies:
            - extractTranscriptText()
    """


    print('First step hi')


def transformData():
    """
        Function to preprocess video data

        Dependencies:
            - handleSpecialStrings()
            - setDatatypes()
    """
    print('Second step hi')

def createTextEmbeddings():
    """
        Function to generate text embeddings of video titles and transcripts
    """
    print('Third step hi')


