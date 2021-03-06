#!/usr/bin/env python
# coding: utf-8

import editconfig
import preprocess
import convert
import hydra
def get_converted_audio(user_id, user_audio_path, org_audio_path) : #아래 함수들을 한번에 실행
    editconfig.speaker_json(user_audio_path, org_audio_path)
    editconfig.train_json(user_audio_path)
    editconfig.test_json(org_audio_path)
    editconfig.synthesis_json(user_id, org_audio_path)
    preprocess.preprocess_dataset()
    hydra._internal.hydra.GlobalHydra().clear()
    convert.convert()
    hydra._internal.hydra.GlobalHydra().clear()
