# helpers for biomedical signal processing, 2025

def grab_file(filename, site_url="https://parralab.org/teaching/biomed-dsp/"):
    import requests
    import io

    PARENT = site_url
    FILENAME = filename
    FULLPATH = PARENT+FILENAME
    print(FULLPATH)

    response = requests.get(FULLPATH)
    data_stream = io.BytesIO(response.content)

    return data_stream


def grab_mat(mat_file):
    from scipy import io as sio

    data_stream = grab_file(mat_file)
    mat_contents = sio.loadmat(data_stream)
    print(mat_contents.keys())

    return mat_contents


def grab_wav(wav_file):
    from scipy import io as sio

    audio_bytes = grab_file(wav_file)
    fs, data = sio.wavfile.read(audio_bytes)

    return fs, data
