"Typed environment configuration for VoiceClone."

from chatenv import BaseEnvConfig, EnvField


class VoicecloneConfig(BaseEnvConfig):
    "VoiceClone ChatEnv configuration."

    _title = "VoiceClone Configuration"
    _aliases = ["voiceclone"]
    _storage_dir = "Voiceclone"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    VOICECLONE_API_KEY = EnvField(
        "VOICECLONE_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["VoicecloneConfig"]
