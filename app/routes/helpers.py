from flask import make_response, abort
import requests
import os

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{model_id} invalid"}, 400))
    
    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"There's no {model_id}, sorry."}, 404))
    return model


        