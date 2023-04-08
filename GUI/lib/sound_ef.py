from playsound import playsound
def Effect(mode):

    ok = 'https://dl4.fara-download.ir/audio/sound_effect/alarms/check/Check%20mark%20sound%20effect.mp3'
    alert = 'https://s3.ir-thr-at1.arvanstorage.ir/soundsnap/5704_metallic_tone_alert_wav_peg7wdv9_watermark?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=a9c0fa52-1a26-4b10-ac1f-49b0d2e5622b%2F20230408%2F%2Fs3%2Faws4_request&X-Amz-Date=20230408T185341Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Signature=4d9dc468f882607fdd4d445a285cbadfa195872fd7e36b45531ef0fb39415ced'

    if mode == 'ok':
        playsound(ok_url)
    elif mode == 'fail':
        playsound(sound)
    elif mode == 'alert':
        playsound(alert_url)