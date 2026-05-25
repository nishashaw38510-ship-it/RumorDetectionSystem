from flask import Blueprint, request, render_template

from model.predict import predict_rumor

from model.url_analyzer import extract_text_from_url

import os

# OPTIONAL OCR
try:

    from model.image_analyzer import extract_text_from_image

    OCR_AVAILABLE = True

except:

    OCR_AVAILABLE = False

prediction_bp = Blueprint(
    'prediction',
    __name__
)

UPLOAD_FOLDER = "static/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

# =========================
# PREDICTION ROUTE
# =========================

@prediction_bp.route(
    '/predict',
    methods=['POST']
)

def predict():

    text = request.form.get(
        'text',
        ''
    ).strip()

    url = request.form.get(
        'url',
        ''
    ).strip()

    image = request.files.get('image')

    analysis_type = "Text Analysis"

    final_input_text = ""

    # =========================
    # TEXT ANALYSIS
    # =========================

    if text:

        final_input_text = text

        analysis_type = "Text Rumor Analysis"

    # =========================
    # URL ANALYSIS
    # =========================

    elif url:

        try:

            extracted_url_text = (
                extract_text_from_url(url)
            )

            final_input_text = extracted_url_text

            analysis_type = "URL Intelligence Analysis"

        except Exception as e:

            final_input_text = (
                f"URL Analysis Failed: {str(e)}"
            )

    # =========================
    # IMAGE ANALYSIS
    # =========================

    elif image and image.filename != "":

        analysis_type = "Image OCR Analysis"

        image_path = os.path.join(
            UPLOAD_FOLDER,
            image.filename
        )

        image.save(image_path)

        if OCR_AVAILABLE:

            try:

                extracted_text = (
                    extract_text_from_image(
                        image_path
                    )
                )

                final_input_text = extracted_text

            except Exception as e:

                final_input_text = (
                    f"OCR Failed: {str(e)}"
                )

        else:

            final_input_text = (
                "OCR Module Not Installed"
            )

    # =========================
    # EMPTY INPUT
    # =========================

    else:

        final_input_text = (
            "No valid content provided."
        )

    # =========================
    # AI PREDICTION
    # =========================

    result = predict_rumor(
        final_input_text
    )

    # =========================
    # RENDER RESULT
    # =========================

    return render_template(

        'result.html',

        analysis_type=analysis_type,

        prediction=result['prediction'],

        confidence=result['confidence'],

        rumor_prob=result['rumor_prob'],

        non_rumor_prob=result['non_rumor_prob'],

        categories=result['categories'],

        threat_level=result['threat_level'],

        alert_signal=result['alert_signal'],

        animation_class=result['animation_class'],

        engagement_score=result['engagement_score'],

        viral_score=result['viral_score'],

        manipulation_index=result['manipulation_index'],

        explanation=result['explanation'],

        user_text=final_input_text
    )