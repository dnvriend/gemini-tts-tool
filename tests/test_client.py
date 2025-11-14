"""Tests for gemini_tts_tool.core.client module.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import os
from unittest.mock import patch

import pytest

from gemini_tts_tool.core.client import AuthenticationError, create_client


def test_create_client_with_api_key() -> None:
    """Test create_client with explicit API key."""
    with patch("gemini_tts_tool.core.client.genai.Client") as mock_client:
        create_client(api_key="test-key-123")
        mock_client.assert_called_once_with(api_key="test-key-123")


def test_create_client_from_google_api_key_env() -> None:
    """Test create_client reads GOOGLE_API_KEY from environment."""
    with patch("gemini_tts_tool.core.client.genai.Client") as mock_client:
        with patch.dict(os.environ, {"GOOGLE_API_KEY": "env-key-456"}, clear=True):
            create_client()
            mock_client.assert_called_once_with(api_key="env-key-456")


def test_create_client_from_gemini_api_key_env() -> None:
    """Test create_client reads GEMINI_API_KEY from environment."""
    with patch("gemini_tts_tool.core.client.genai.Client") as mock_client:
        with patch.dict(os.environ, {"GEMINI_API_KEY": "gemini-key-789"}, clear=True):
            create_client()
            mock_client.assert_called_once_with(api_key="gemini-key-789")


def test_create_client_google_api_key_precedence() -> None:
    """Test GOOGLE_API_KEY takes precedence over GEMINI_API_KEY."""
    with patch("gemini_tts_tool.core.client.genai.Client") as mock_client:
        with patch.dict(
            os.environ,
            {"GOOGLE_API_KEY": "google-key", "GEMINI_API_KEY": "gemini-key"},
            clear=True,
        ):
            create_client()
            # Should use GOOGLE_API_KEY
            mock_client.assert_called_once_with(api_key="google-key")


def test_create_client_no_api_key_raises_error() -> None:
    """Test create_client raises error when no API key available."""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(AuthenticationError, match="API key is required"):
            create_client()


def test_create_client_error_message_helpful() -> None:
    """Test create_client error message contains helpful information."""
    with patch.dict(os.environ, {}, clear=True):
        try:
            create_client()
            assert False, "Should have raised AuthenticationError"
        except AuthenticationError as e:
            error_msg = str(e)
            assert "GEMINI_API_KEY" in error_msg
            assert "GOOGLE_API_KEY" in error_msg
            assert "aistudio.google.com" in error_msg


def test_create_client_vertex_ai() -> None:
    """Test create_client with Vertex AI configuration."""
    with patch("gemini_tts_tool.core.client.genai.Client") as mock_client:
        with patch.dict(
            os.environ, {"GOOGLE_GENAI_USE_VERTEXAI": "true", "GOOGLE_CLOUD_PROJECT": "my-project"}
        ):
            create_client(use_vertex=True, project="test-project", location="us-central1")
            mock_client.assert_called_once_with(
                vertexai=True, project="test-project", location="us-central1"
            )


def test_create_client_vertex_ai_from_env() -> None:
    """Test create_client reads Vertex AI config from environment."""
    with patch("gemini_tts_tool.core.client.genai.Client") as mock_client:
        with patch.dict(
            os.environ,
            {
                "GOOGLE_GENAI_USE_VERTEXAI": "true",
                "GOOGLE_CLOUD_PROJECT": "env-project",
                "GOOGLE_CLOUD_LOCATION": "europe-west1",
            },
            clear=True,
        ):
            create_client()
            mock_client.assert_called_once_with(
                vertexai=True, project="env-project", location="europe-west1"
            )


def test_create_client_vertex_ai_no_project_raises_error() -> None:
    """Test create_client raises error when Vertex AI enabled but no project."""
    with patch.dict(os.environ, {"GOOGLE_GENAI_USE_VERTEXAI": "true"}, clear=True):
        with pytest.raises(
            AuthenticationError, match="GOOGLE_CLOUD_PROJECT.*required for Vertex AI"
        ):
            create_client(use_vertex=True)


def test_create_client_vertex_ai_error_message_helpful() -> None:
    """Test Vertex AI error message contains helpful information."""
    with patch.dict(os.environ, {"GOOGLE_GENAI_USE_VERTEXAI": "true"}, clear=True):
        try:
            create_client(use_vertex=True)
            assert False, "Should have raised AuthenticationError"
        except AuthenticationError as e:
            error_msg = str(e)
            assert "GOOGLE_CLOUD_PROJECT" in error_msg
