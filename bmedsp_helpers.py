# helpers for biomedical signal processing, 2025

def grab_file(filename, site_url="https://parralab.org/teaching/biomed-dsp/"):
    """
    used in grab_mat() and grab_wav() methods
    """
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
    """
    returns: matlab file data and metadata
    """
    from scipy import io as sio

    data_stream = grab_file(mat_file)
    mat_contents = sio.loadmat(data_stream)
    print(mat_contents.keys())
    if '__header__' in mat_contents:
        print(mat_contents['__header__'])

    return mat_contents


def grab_wav(wav_file):
    """
    returns: sample rate (fs) and wav file data (data)
    """
    from scipy import io as sio

    audio_bytes = grab_file(wav_file)
    fs, data = sio.wavfile.read(audio_bytes)

    return fs, data


def est_ma_filter(sig_in, sig_out, Q):
    from scipy.linalg import toeplitz
    x = sig_in
    y = sig_out
    n_coeffs = Q+1

    # avoid edge artifacts
    y_vec = y[Q:]
    col = x[Q:]
    row = x[Q::-1][:n_coeffs]

    X = toeplitz(col, row)
    b_hat, _, _, _ = np.linalg.lstsq(X, y_vec)

    return b_hat


def gaborfir(fc, fs, Q):
    """
    fc: center freq in Hz
    fs:
    Q: quality factor, bw relative to center freq

    implements lucas' MATLAB Gabor function:
        function b=gaborfir(fc,fs,Q)
            df = fc/Q; % bandwidth in Hz,
            dt = 1/df;
            t = (-3*dt*fs:3*dt*fs)'/fs;
            b = 1/sqrt(pi/2)/fs/dt*exp(-t.^2/2/dt^2).*exp(sqrt(-1)*2*pi*fc*t);
    """
    df = fc/Q  # bandwidth in Hz
    dt = 1/df  # t const related to gauss env spread

    # t = (-3*dt*fs:3*dt*fs)'/fs;
    t_start = -3 * dt * fs
    t_end = 3 * dt * fs

    t_idx = np.arange(np.ceil(t_start), np.floor(t_end) + 1)
    t = t_idx / fs # s

    # b = (1 / sqrt(pi/2) / fs / dt) * exp(-t^2 / (2*dt^2)) * exp(i * 2*pi*fc*t)
    term1 = 1 / (np.sqrt(np.pi / 2) * fs * dt) # normalization factor?
    term2 = np.exp(-t**2 / (2 * dt**2)) # gaussian envelope
    term3 = np.exp(1j * 2 * np.pi * fc * t) # carrier wave

    b = term1 * term2 * term3
    return b


def spacer_and_ylimits(x_orig, spacer_factor=1.1, margin_factor=0.05, min_absolute_spacer=0.1, min_absolute_margin=0.1):
    """
    plots multiple series, evenly spaced plus margins - use without pyplot yticks
    returns:
      spacer: spacing between series
      ylimits: some buffer added to y-axis limits based on max/min after spacing
    """
    import numpy as np
    
    H = 0
    for x in x_orig:
        H = max(H, (np.max(x) - np.min(x)))
    spacer = H * spacer_factor

    y_shifted = []
    for i, x in enumerate(x_orig):
        y_shifted.extend([y + i*spacer for y in x])

    margin = (np.max(y_shifted) - np.min(y_shifted)) * margin_factor
    ymin = np.min(y_shifted) - margin
    ymax = np.max(y_shifted) + margin
    ylimits = (ymin, ymax)

    return spacer, ylimits
