

language_data = {
    "english": {
        "description": """
        ### 🎥 **Project Created By VIT Students!** 📽️

        Upload a video, subtitle, audio file or provide a URL video link. 📽️ 
        See the tab `Help` for instructions on how to use it. Let's start having fun with video translation! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Instructions for use:**

        1. 📤 Upload a **video**, **subtitle file**, **audio file**, or provide a 🌐 **URL link** to a video like YouTube.

        2. 🌍 Choose the language in which you want to **translate the video**.

        3. 🗣️ Specify the **number of people speaking** in the video and **assign each one a text-to-speech voice** suitable for the translation language.

        4. 🚀 Press the '**Translate**' button to obtain the results.

        ---

        # 🧩 **SoniTranslate supports different TTS (Text-to-Speech) engines, which are:**
        - EDGE-TTS → format `en-AU-WilliamNeural-Male` → Fast and accurate.
        - FACEBOOK MMS → format `en-facebook-mms VITS` → The voice is more natural; at the moment, it only uses CPU.
        - PIPER TTS → format `en_US-lessac-high VITS-onnx` → Same as the previous one, but it is optimized for both CPU and GPU.
        - BARK → format `en_speaker_0-Male BARK` → Good quality but slow, and it is prone to hallucinations.
        - OpenAI TTS → format `>alloy OpenAI-TTS` → Multilingual but it needs an OpenAI API key.
        - Coqui XTTS → format `_XTTS_/AUTOMATIC.wav` → Only available for Chinese (Simplified), English, French, German, Italian, Portuguese, Polish, Turkish, Russian, Dutch, Czech, Arabic, Spanish, Hungarian, Korean and Japanese.

        ---

        # 🎤 How to Use R.V.C. and R.V.C.2 Voices (Optional) 🎶

        The goal is to apply a R.V.C. to the generated TTS (Text-to-Speech) 🎙️

        1. In the `Custom Voice R.V.C.` tab, download the models you need 📥 You can use links from Hugging Face and Google Drive in formats like zip, pth, or index. You can also download complete HF space repositories, but this option is not very stable 😕

        2. Now, go to `Replace voice: TTS to R.V.C.` and check the `enable` box ✅ After this, you can choose the models you want to apply to each TTS speaker 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Adjust the F0 method that will be applied to all R.V.C. 🎛️

        4. Press `APPLY CONFIGURATION` to apply the changes you made 🔄

        5. Go back to the video translation tab and click on 'Translate' ▶️ Now, the translation will be done applying the R.V.C. 🗣️

        Tip: You can use `Test R.V.C.` to experiment and find the best TTS or configurations to apply to the R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Video translation",
        "video_source": "Choose Video Source",
        "link_label": "Media link.",
        "link_info": "Example: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL goes here...",
        "dir_label": "Video Path.",
        "dir_info": "Example: /usr/home/my_video.mp4",
        "dir_ph": "Path goes here...",
        "sl_label": "Source language",
        "sl_info": "This is the original language of the video",
        "tat_label": "Translate audio to",
        "tat_info": "Select the target language and also make sure to choose the corresponding TTS for that language.",
        "num_speakers": "Select how many people are speaking in the video.",
        "min_sk": "Min speakers",
        "max_sk": "Max speakers",
        "tts_select": "Select the voice you want for each speaker.",
        "sk1": "TTS Speaker 1",
        "sk2": "TTS Speaker 2",
        "sk3": "TTS Speaker 3",
        "sk4": "TTS Speaker 4",
        "sk5": "TTS Speaker 5",
        "sk6": "TTS Speaker 6",
        "sk7": "TTS Speaker 7",
        "sk8": "TTS Speaker 8",
        "sk9": "TTS Speaker 9",
        "sk10": "TTS Speaker 10",
        "sk11": "TTS Speaker 11",
        "sk12": "TTS Speaker 12",
        "vc_title": "Voice Imitation in Different Languages",
        "vc_subtitle": """
        ### Replicate a person's voice across various languages.
        While effective with most voices when used appropriately, it may not achieve perfection in every case.
        Voice Imitation solely replicates the reference speaker's tone, excluding accent and emotion, which are governed by the base speaker TTS model and not replicated by the converter.
        This will take audio samples from the main audio for each speaker and process them.
        """,
        "vc_active_label": "Active Voice Imitation",
        "vc_active_info": "Active Voice Imitation: Replicates the original speaker's tone",
        "vc_method_label": "Method",
        "vc_method_info": "Select a method for Voice Imitation process",
        "vc_segments_label": "Max samples",
        "vc_segments_info": "Max samples: Is the number of audio samples that will be generated for the process, more is better but it can add noise",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Applies vocal dereverb to the audio samples.",
        "vc_remove_label": "Remove previous samples",
        "vc_remove_info": "Remove previous samples: Remove the previous samples generated, so new ones need to be created.",
        "xtts_title": "Create a TTS based on an audio",
        "xtts_subtitle": "Upload an audio file of maximum 10 seconds with a voice. Using XTTS, a new TTS will be created with a voice similar to the provided audio file.",
        "xtts_file_label": "Upload a short audio with the voice",
        "xtts_name_label": "Name for the TTS",
        "xtts_name_info": "Use a simple name",
        "xtts_dereverb_label": "Dereverb audio",
        "xtts_dereverb_info": "Dereverb audio: Applies vocal dereverb to the audio",
        "xtts_button": "Process the audio and include it in the TTS selector",
        "xtts_footer": "Generate voice xtts automatically: You can use `_XTTS_/AUTOMATIC.wav` in the TTS selector to automatically generate segments for each speaker when generating the translation.",
        "extra_setting": "Advanced Settings",
        "acc_max_label": "Max Audio acceleration",
        "acc_max_info": "Maximum acceleration for translated audio segments to avoid overlapping. A value of 1.0 represents no acceleration",
        "acc_rate_label": "Acceleration Rate Regulation",
        "acc_rate_info": "Acceleration Rate Regulation: Adjusts acceleration to accommodate segments requiring less speed, maintaining continuity and considering next-start timing.",
        "or_label": "Overlap Reduction",
        "or_info": "Overlap Reduction: Ensures segments don't overlap by adjusting start times based on previous end times; could disrupt synchronization.",
        "aud_mix_label": "Audio Mixing Method",
        "aud_mix_info": "Mix original and translated audio files to create a customized, balanced output with two available mixing modes.",
        "vol_ori": "Volume original audio",
        "vol_tra": "Volume translated audio",
        "voiceless_tk_label": "Voiceless Track",
        "voiceless_tk_info": "Voiceless Track: Remove the original audio voices before combining it with the translated audio.",
        "sub_type": "Subtitle type",
        "soft_subs_label": "Soft Subtitles",
        "soft_subs_info": "Soft Subtitles: Optional subtitles that viewers can turn on or off while watching the video.",
        "burn_subs_label": "Burn Subtitles",
        "burn_subs_info": "Burn Subtitles: Embed subtitles into the video, making them a permanent part of the visual content.",
        "whisper_title": "Config transcription.",
        "lnum_label": "Literalize Numbers",
        "lnum_info": "Literalize Numbers: Replace numerical representations with their written equivalents in the transcript.",
        "scle_label": "Sound Cleanup",
        "scle_info": "Sound Cleanup: Enhance vocals, remove background noise before transcription for utmost timestamp precision. This operation may take time, especially with lengthy audio files.",
        "sd_limit_label": "Segment Duration Limit",
        "sd_limit_info": "Specify the maximum duration (in seconds) for each segment. The audio will be processed using VAD, limiting the duration for each segment chunk.",
        "asr_model_info": "It converts spoken language to text using the 'Whisper model' by default. Use a custom model, for example, by inputting the repository name 'BELLE-2/Belle-whisper-large-v3-zh' in the dropdown to utilize a Chinese language finetuned model. Find finetuned models on Hugging Face.",
        "ctype_label": "Compute type",
        "ctype_info": "Choosing smaller types like int8 or float16 can improve performance by reducing memory usage and increasing computational throughput, but may sacrifice precision compared to larger data types like float32.",
        "batchz_label": "Batch size",
        "batchz_info": "Reducing the batch size saves memory if your GPU has less VRAM and helps manage Out of Memory issues.",
        "tsscale_label": "Text Segmentation Scale",
        "tsscale_info": "Divide text into segments by sentences, words, or characters. Word and character segmentation offer finer granularity, useful for subtitles; disabling translation preserves original structure.",
        "srt_file_label": "Upload an SRT subtitle file (will be used instead of the transcription of Whisper)",
        "divide_text_label": "Redivide text segments by:",
        "divide_text_info": "(Experimental) Enter a separator to split existing text segments in the source language. The tool will identify occurrences and create new segments accordingly. Specify multiple separators using |, e.g.: !|?|...|。",
        "diarization_label": "Diarization model",
        "tr_process_label": "Translation process",
        "out_type_label": "Output type",
        "out_name_label": "File name",
        "out_name_info": "The name of the output file",
        "task_sound_label": "Task Status Sound",
        "task_sound_info": "Task Status Sound: Plays a sound alert indicating task completion or errors during execution.",
        "cache_label": "Retrieve Progress",
        "cache_info": "Retrieve Progress: Continue process from last checkpoint.",
        "preview_info": "Preview cuts the video to only 10 seconds for testing purposes. Please deactivate it to retrieve the full video duration.",
        "edit_sub_label": "Edit generated subtitles",
        "edit_sub_info": "Edit generated subtitles: Allows you to run the translation in 2 steps. First with the 'GET SUBTITLES AND EDIT' button, you get the subtitles to edit them, and then with the 'TRANSLATE' button, you can generate the video",
        "button_subs": "GET SUBTITLES AND EDIT",
        "editor_sub_label": "Generated subtitles",
        "editor_sub_info": "Feel free to edit the text in the generated subtitles here. You can make changes to the interface options before clicking the 'TRANSLATE' button, except for 'Source language', 'Translate audio to', and 'Max speakers', to avoid errors. Once you're finished, click the 'TRANSLATE' button.",
        "editor_sub_ph": "First press 'GET SUBTITLES AND EDIT' to get the subtitles",
        "button_translate": "TRANSLATE",
        "output_result_label": "DOWNLOAD TRANSLATED VIDEO",
        "sub_ori": "Subtitles",
        "sub_tra": "Translated subtitles",
        "ht_token_info": "One important step is to accept the license agreement for using Pyannote. You need to have an account on Hugging Face and accept the license to use the models: https://huggingface.co/pyannote/speaker-diarization and https://huggingface.co/pyannote/segmentation. Get your KEY TOKEN here: https://hf.co/settings/tokens",
        "ht_token_ph": "Token goes here...",
        "tab_docs": "Document translation",
        "docs_input_label": "Choose Document Source",
        "docs_input_info": "It can be PDF, DOCX, TXT, or text",
        "docs_source_info": "This is the original language of the text",
        "chunk_size_label": "Max number of characters that the TTS will process per segment",
        "chunk_size_info": "A value of 0 assigns a dynamic and more compatible value for the TTS.",
        "docs_button": "Start Language Conversion Bridge",
        "cv_url_info": "Automatically download the R.V.C. models from the URL. You can use links from HuggingFace or Drive, and you can include several links, each one separated by a comma. Example: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Replace voice: TTS to R.V.C.",
        "sec1_title": "### 1. To enable its use, mark it as enable.",
        "enable_replace": "Check this to enable the use of the models.",
        "sec2_title": "### 2. Select a voice that will be applied to each TTS of each corresponding speaker and apply the configurations.",
        "sec2_subtitle": "Depending on how many <TTS Speaker> you will use, each one needs its respective model. Additionally, there is an auxiliary one if for some reason the speaker is not detected correctly.",
        "cv_tts1": "Choose the voice to apply for Speaker 1.",
        "cv_tts2": "Choose the voice to apply for Speaker 2.",
        "cv_tts3": "Choose the voice to apply for Speaker 3.",
        "cv_tts4": "Choose the voice to apply for Speaker 4.",
        "cv_tts5": "Choose the voice to apply for Speaker 5.",
        "cv_tts6": "Choose the voice to apply for Speaker 6.",
        "cv_tts7": "Choose the voice to apply for Speaker 7.",
        "cv_tts8": "Choose the voice to apply for Speaker 8.",
        "cv_tts9": "Choose the voice to apply for Speaker 9.",
        "cv_tts10": "Choose the voice to apply for Speaker 10.",
        "cv_tts11": "Choose the voice to apply for Speaker 11.",
        "cv_tts12": "Choose the voice to apply for Speaker 12.",
        "cv_aux": "- Voice to apply in case a Speaker is not detected successfully.",
        "cv_button_apply": "APPLY CONFIGURATION",
        "tab_help": "Help",
    },

    "hindi": {
        "description": """
          ### 🎥 **VIT के छात्रो द्वारा एक प्रोजेक्ट ** 📽️

          एक वीडियो, ऑडियो फ़ाइल अपलोड करें या एक YouTube लिंक प्रदान करें। 📽️ **आधिकारिक भंडार से अपडेटेड नोटबुक प्राप्त करें: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

          उसे 'मदद' टैब देखें इसका उपयोग कैसे करना है के निर्देशों के लिए। वीडियो अनुवाद के साथ मज़े करना शुरू करें! 🚀🎉
          """,
        "tutorial": """
          # 🔰 **उपयोग के लिए निर्देश:**

          1. 📤 **वीडियो**, **ऑडियो फ़ाइल** अपलोड करें या एक 🌐 **YouTube लिंक** प्रदान करें।

          2. 🌍 चुनें कि आप किस भाषा में **वीडियो को अनुवादित** करना चाहते हैं।

          3. 🗣️ वीडियो में **बोलने वाले लोगों की संख्या** और **प्रत्येक को टेक्स्ट-टू-स्पीच आवाज** देने का निर्देश दें, जो अनुवाद भाषा के लिए उपयुक्त है।

          4. 🚀 '**अनुवाद**' बटन दबाएं और परिणाम प्राप्त करें।

          ---

          # 🧩 **SoniTranslate विभिन्न TTS (टेक्स्ट-टू-स्पीच) इंजनों का समर्थन करता है, जो हैं:**
          - EDGE-TTS → प्रारूप `en-AU-WilliamNeural-Male` → तेज़ और सटीक।
          - FACEBOOK MMS → प्रारूप `en-facebook-mms VITS` → आवाज अधिक प्राकृतिक है; वर्तमान में, यह केवल CPU का उपयोग करता है।
          - PIPER TTS → प्रारूप `en_US-lessac-high VITS-onnx` → पिछले वाले के समान, लेकिन यह CPU और GPU दोनों के लिए अनुकूलित है।
          - BARK → प्रारूप `en_speaker_0-Male BARK` → अच्छी गुणवत्ता है लेकिन धीमी, और यह हैलुसिनेशन के लिए प्रवृत्त है।
          - OpenAI TTS → प्रारूप `>alloy OpenAI-TTS` → बहुभाषी लेकिन इसमें एक OpenAI API key की आवश्यकता है
          - Coqui XTTS → प्रारूप `_XTTS_/AUTOMATIC.wav` → केवल चीनी (सरलीकृत), अंग्रेजी, फ्रेंच, जर्मन, इतालवी, पुर्तगाली, पोलिश, तुर्की, रूसी, डच, चेक, अरबी, स्पैनिश, हंगेरियन, कोरियाई और जापानी के लिए ही उपलब्ध है।

          ---

          # 🎤 R.V.C. और R.V.C.2 आवाज़ों का उपयोग कैसे करें (वैकल्पिक) 🎶

          लक्ष्य है कि जेनेरेटेड TTS (टेक्स्ट-टू-स्पीच) पर एक R.V.C. लागू करें 🎙️

          1. `कस्टम आवाज़ आर.वी.सी.` टैब में, आपको आवश्यक मॉडल डाउनलोड करने की आवश्यकता है 📥 आप हग्गिंग फेस और गूगल ड्राइव से लिंक्स का उपयोग कर सकते हैं जैसे zip, pth, या इंडेक्स के प्रारूप में। आप पूरे एचएफ स्पेस रिपॉज़िटरी को भी डाउनलोड कर सकते हैं, लेकिन यह विकल्प बहुत ही अस्थिर है 😕

          2. अब, `आवाज़ बदलें: TTS से R.V.C.` पर जाएं और `सक्रिय` बॉक्स को चेक करें ✅ इसके बाद, आप प्रत्येक TTS बोलने वाले को लागू करने के लिए जो आप चाहते हैं उसे चुन सकते हैं 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

          3. सभी R.V.C. पर लागू किया जाने वाला F0 विधि समायोजित करें 🎛️

          4. आपके द्वारा किए गए परिवर्तनों को लागू करने के लिए `आवेदन को लागू करें` दबाएं 🔄

          5. वीडियो अनुवाद टैब पर वापस जाएं और 'अनुवाद करें' पर क्लिक करें ▶️ अब, अनुवाद R.V.C. को लागू करते हुए किया जाएगा। 🗣️

          सुझाव: आप `टेस्ट R.V.C.` का उपयोग करके प्रयोग कर सकते हैं और R.V.C. को लागू करने के लिए सर्वोत्तम TTS या कॉन्फ़िगरेशन खोज सकते हैं। 🧪🔍

          ---

          """,
        "tab_translate": "वीडियो अनुवाद",
        "video_source": "वीडियो स्रोत चुनें",
        "link_label": "मीडिया लिंक।",
        "link_info": "उदाहरण: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL यहाँ डालें...",
        "dir_label": "वीडियो पथ।",
        "dir_info": "उदाहरण: /usr/home/my_video.mp4",
        "dir_ph": "पथ यहाँ डालें...",
        "sl_label": "स्रोत भाषा",
        "sl_info": "यह वीडियो की मूल भाषा है",
        "tat_label": "ऑडियो को अनुवाद करें",
        "tat_info": "लक्ष्य भाषा का चयन करें और सुनिश्चित करें कि उस भाषा के लिए संबंधित TTS चुना गया है।",
        "num_speakers": "वीडियो में कितने लोग बोल रहे हैं, उन्हें चुनें।",
        "min_sk": "न्यूनतम बोलने वाले",
        "max_sk": "अधिकतम बोलने वाले",
        "tts_select": "प्रत्येक बोलने वाले के लिए आप जो आवाज़ चाहते हैं, उसे चुनें।",
        "sk1": "TTS बोलने वाला 1",
        "sk2": "TTS बोलने वाला 2",
        "sk3": "TTS बोलने वाला 3",
        "sk4": "TTS बोलने वाला 4",
        "sk5": "TTS बोलने वाला 5",
        "sk6": "TTS बोलने वाला 6",
        "sk7": "TTS बोलने वाला 7",
        "sk8": "TTS बोलने वाला 8",
        "sk9": "TTS बोलने वाला 9",
        "sk10": "TTS बोलने वाला 10",
        "sk11": "TTS बोलने वाला 11",
        "sk12": "TTS बोलने वाला 12",
        "vc_title": "विभिन्न भाषाओं में आवाज़ का नकल",
        "vc_subtitle": """
          ### विभिन्न भाषाओं में एक व्यक्ति की आवाज़ का नकल।
          जब सही ढंग से प्रयोग किया जाता है, तो अधिकांश आवाज़ों के साथ प्रभावी है, लेकिन हर मामले में पूर्णता को हासिल नहीं कर सकता है।
          आवाज़ का नकल केवल संदर्भ वक्ता के टोन को प्रतिलिपि करता है, एक्सेंट और भावना को बाहर करता है, जो आधार वक्ता TTS मॉडल द्वारा नियंत्रित होता है और कनवर्टर द्वारा प्रतिलिपि नहीं किया जाता है।
          यह मुख्य ऑडियो के लिए ऑडियो नमूने लेता है और प्रसंस्करण करता है।
          """,
        "vc_active_label": "सक्रिय आवाज़ का नकल",
        "vc_active_info": "सक्रिय आवाज़ का नकल: मूल बोलने वाले के टोन को प्रतिलिपि करता है",
        "vc_method_label": "विधि",
        "vc_method_info": "आवाज़ का नकल प्रक्रिया के लिए एक विधि का चयन करें",
        "vc_segments_label": "अधिकतम सैंपल",
        "vc_segments_info": "अधिकतम सैंपल: प्रक्रिया के लिए ऑडियो सैंपलों की संख्या है, अधिक बेहतर है, लेकिन यह शोर जोड़ सकता है",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: ऑडियो सैंपलों पर ध्वनि dereverb लागू करता है।",
        "vc_remove_label": "पिछले सैंपल हटाएं",
        "vc_remove_info": "पिछले सैंपल हटाएं: पिछले सैंपल हटा देता है: ताकि नए सैंपल उत्पन्न किए जाने की आवश्यकता हो।",
        "xtts_title": "ऑडियो पर आधारित TTS बनाएं",
        "xtts_subtitle": "एक ऑडियो फ़ाइल को अधिकतम 10 सेकंड के साथ एक आवाज़ के साथ अपलोड करें। XTTS का उपयोग करके, एक नया TTS बनाया जाएगा जो प्रदान की गई ऑडियो फ़ाइल के समान होगा।",
        "xtts_file_label": "आवाज़ के साथ एक छोटा ऑडियो अपलोड करें",
        "xtts_name_label": "TTS के लिए नाम",
        "xtts_name_info": "एक सरल नाम का उपयोग करें",
        "xtts_dereverb_label": "Dereverb ऑडियो",
        "xtts_dereverb_info": "Dereverb ऑडियो: ऑडियो पर ध्वनि dereverb लागू करें",
        "xtts_button": "ऑडियो प्रक्रिया करें और इसे TTS सेलेक्टर में शामिल करें",
        "xtts_footer": "स्वचालित रूप से आवाज़ xtts उत्पन्न करें: अनुवाद उत्पन्न करते समय प्रत्येक बोलने वाले के लिए सेगमेंट ऑटोमेटिकली उत्पन्न करने के लिए आप `_XTTS_/AUTOMATIC.wav` का उपयोग कर सकते हैं।",
        "extra_setting": "उन्नत सेटिंग्स",
        "acc_max_label": "अधिकतम ऑडियो त्वरण",
        "acc_max_info": "ओवरलैपिंग से बचने के लिए अनुवादित ऑडियो सेगमेंटों के लिए अधिकतम त्वरण। 1.0 का मान कोई त्वरण नहीं दर्शाता है।",
        "acc_rate_label": "त्वरण दर नियामक",
        "acc_rate_info": "त्वरण दर नियामक: त्वरण को समायोजित करता है ताकि उपभागों को उससे कम गति की आवश्यकता हो, सततता को बनाए रखते हुए और अगले आरंभ के समय को ध्यान में रखते हुए।",
        "or_label": "ओवरलैप कमी करना",
        "or_info": "ओवरलैप कमी करना: पिछले समाप्ति समयों के आधार पर शुरुआत समयों को समायोजित करके सेगमेंट को ओवरलैप नहीं होने देता है; समवारण को बिगाड़ सकता है।",
        "aud_mix_label": "ऑडियो मिश्रण विधि",
        "aud_mix_info": "मूल और अनुवादित ऑडियो फ़ाइलों को मिश्रित करें और दो उपलब्ध मिश्रण मोड के साथ एक अनुकूलित, संतुलित उत्पादन बनाएं।",
        "vol_ori": "मूल ऑडियो ध्वनि",
        "vol_tra": "अनुवादित ऑडियो ध्वनि",
        "voiceless_tk_label": "वॉइसलेस ट्रैक",
        "voiceless_tk_info": "अनुवादित ऑडियो के साथ इसे मिलाने से पहले मूल ऑडियो ध्वनियों को हटाएं।",
        "sub_type": "उपशीर्षक प्रकार",
        "soft_subs_label": "मुलायम सबटाइटल्स",
        "soft_subs_info": "मुलायम सबटाइटल्स: व्यूअर्स वीडियो देखते समय चाहें तो चालू या बंद कर सकते हैं।",
        "burn_subs_label": "उपशीर्षक जलाएं",
        "burn_subs_info": "उपशीर्षक जलाएं: वीडियो में उपशीर्षक एम्बेड करें, जिससे वे दृश्यीय सामग्री का स्थायी हिस्सा बन जाएं।",
        "whisper_title": "कॉन्फ़िगर ट्रांस्क्रिप्शन।",
        "lnum_label": "संख्याओं का वाचक रूपांतरण",
        "lnum_info": "संख्याओं का वाचक रूपांतरण: संख्यात्मक प्रतिनिधित्वों को उनके लेखित समकक्षों से प्रतिस्थापित करें ट्रांसक्रिप्ट में।",
        "scle_label": "ध्वनि की सफाई",
        "scle_info": "ध्वनि की सफाई: अधिकतम समयचिह्न सटीकता के लिए ध्वनि को बेहतर बनाएं, समय चिह्नों की अधिकता के लिए अधिकतम समयचिह्न सटीकता के लिए पीछे की ध्वनि हटाएं। इस ऑपरेशन में समय लग सकता है, खासकर लंबे ऑडियो फ़ाइलों के साथ।",
        "sd_limit_label": "सेगमेंट अवधि सीमा",
        "sd_limit_info": "प्रत्येक सेगमेंट की अधिकतम अवधि (सेकंड में) को निर्दिष्ट करें। ऑडियो को वैड का उपयोग करके प्रोसेस किया जाएगा, प्रत्येक सेगमेंट चंक की अवधि को सीमित करके।",
        "asr_model_info": "यह डिफ़ॉल्ट रूप से बोली भाषा को पाठ में परिवर्तित करता है 'व्हिस्पर मॉडल' का उपयोग करके। अपना कस्टम मॉडल उपयोग करें, उदाहरण के लिए, ड्रॉपडाउन में रिपॉज़िटरी नाम 'BELLE-2/Belle-whisper-large-v3-zh' दर्ज करके एक चीनी भाषा फ़ाइन ट्यून मॉडल का उपयोग करें। Hugging Face पर फ़ाइन ट्यून मॉडल्स पाएँ।",
        "ctype_label": "हिसाब प्रकार",
        "ctype_info": "छोटे प्रकारों जैसे int8 या फ़्लोट16 का चयन करना प्रदर्शन को बढ़ावा दे सकता है, मेमोरी उपयोग को कम करके और गणनात्मक परिचालन बढ़ाकर प्रदर्शन को सुधार सकता है, लेकिन float32 जैसे बड़े डेटा प्रकारों की तुलना में निश्चितता को कट्टरता में बदल सकता है।",
        "batchz_label": "बैच का आकार",
        "batchz_info": "यदि आपके पास कम VRAM वाली जीपीयू है, तो बैच का आकार कम करने से मेमोरी बचाई जा सकती है और मेमोरी की कमी की समस्याओं का प्रबंधन किया जा सकता है।",
        "tsscale_label": "पाठ के विभाजन का पैमाना",
        "tsscale_info": "पाठ को वाक्य, शब्द या अक्षरों के आधार पर खंडों में विभाजित करें। शब्द और अक्षर विभाजन और लघु ग्रेन्युलरिटी प्रदान करता है, जो उपशीर्षकों के लिए उपयोगी है; अनुवाद को अक्षम करने से मूल संरचना को संरक्षित रखा जाता है।",
        "srt_file_label": "एक SRT उपशीर्षक फ़ाइल अपलोड करें (विस्पर की प्रतिलिपि के बजाय इस्तेमाल की जाएगी)",
        "divide_text_label": "पुनः विभाजित करें टेक्स्ट सेगमेंट द्वारा:",
        "divide_text_info": "(प्रयोगात्मक) मौजूदा पाठ सेगमेंट को विभाजित करने के लिए एक विभाजक दर्ज करें। उपकरण को घटनाओं को पहचानने और उन्हें अनुसार नए सेगमेंट बनाने के लिए। | का उपयोग करके एक से अधिक विभाजक निर्दिष्ट करें, उदा।: !|?|...|。",
        "diarization_label": "डायरिज़ेशन मॉडल",
        "tr_process_label": "अनुवाद प्रक्रिया",
        "out_type_label": "आउटपुट प्रकार",
        "out_name_label": "फ़ाइल का नाम",
        "out_name_info": "आउटपुट फ़ाइल का नाम",
        "task_sound_label": "कार्य स्थिति ध्वनि",
        "task_sound_info": "कार्य स्थिति ध्वनि: कार्य समाप्ति या क्रिया के दौरान त्रुटियों की सूचना देने वाला ध्वनि चलाता है।",
        "cache_label": "प्रगति पुनः प्राप्त करें",
        "cache_info": "प्रगति पुनः प्राप्त करें: पिछले चेकप्वाइंट से प्रक्रिया जारी रखें।",
        "preview_info": "पूर्णत: अधिकतम 10 सेकंड के लिए वीडियो काटता है परीक्षण के उद्देश्यों के लिए। कृपया इसे निष्क्रिय करें ताकि पूरा वीडियो अवधि प्राप्त की जा सके।",
        "edit_sub_label": "उत्पन्न उपशीर्षक संपादित करें",
        "edit_sub_info": "उत्पन्न उपशीर्षक संपादित करें: आपको 2 चरणों में अनुवाद चलाने की अनुमति देता है। पहले 'GET SUBTITLES AND EDIT' बटन के साथ, आप उन्हें संपादित करने के लिए उपशीर्षक प्राप्त करते हैं, और फिर 'TRANSLATE' बटन के साथ, आप वीडियो उत्पन्न कर सकते हैं",
        "button_subs": "GET SUBTITLES AND EDIT",
        "editor_sub_label": "उत्पन्न उपशीर्षक",
        "editor_sub_info": "यहाँ उत्पन्न उपशीर्षक में पाठ संपादित करने के लिए स्वतंत्र महसूस करें। आप इंटरफ़ेस विकल्पों में परिवर्तन कर सकते हैं, 'TRANSLATE' बटन पर क्लिक करने से पहले, 'Source language', 'Translate audio to' और 'Max speakers', त्रुटियों से बचने के लिए, 'TRANSLATE' बटन पर क्लिक करें। जब आप समाप्त हो जाएं, 'TRANSLATE' बटन पर क्लिक करें।",
        "editor_sub_ph": "पहले 'GET SUBTITLES AND EDIT' दबाएं ताकि उपशीर्षक प्राप्त हो",
        "button_translate": "TRANSLATE",
        "output_result_label": "अनुवादित वीडियो डाउनलोड करें",
        "sub_ori": "उपशीर्षक",
        "sub_tra": "अनुवादित उपशीर्षक",
        "ht_token_info": "एक महत्वपूर्ण कदम है प्यानोट का उपयोग करने के लिए लाइसेंस समझ। आपको Hugging Face पर एक खाता होना चाहिए और मॉडल का उपयोग करने के लिए लाइसेंस स्वीकार करने की आवश्यकता है: https://huggingface.co/pyannote/speaker-diarization और https://huggingface.co/pyannote/segmentation। अपना KEY TOKEN यहाँ प्राप्त करें: https://hf.co/settings/tokens",
        "ht_token_ph": "टोकन यहाँ जाता है...",
        "tab_docs": "दस्तावेज़ अनुवाद",
        "docs_input_label": "दस्तावेज़ स्रोत चुनें",
        "docs_input_info": "यह PDF, DOCX, TXT, या पाठ हो सकता है",
        "docs_source_info": "यह पाठ की मूल भाषा है",
        "chunk_size_label": "प्रति सेगमेंट TTS द्वारा प्रसंस्कृत किए जाने वाले अधिकतम अक्षरों की संख्या",
        "chunk_size_info": "0 का मान एक गतिशील और और संगतिपूर्ण मान को TTS के लिए सौंपता है।",
        "docs_button": "भाषा परिवर्तन सेतु शुरू करें",
        "cv_url_info": "URL से R.V.C. मॉडल आपमूर्त डाउनलोड करें। आप HuggingFace या Drive से लिंक का उपयोग कर सकते हैं, और आप कई लिंक शामिल कर सकते हैं, प्रत्येक को अल्पविराम द्वारा अलग किया जा सकता है। उदाहरण: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "आवाज़ को बदलें: TTS से R.V.C.",
        "sec1_title": "### 1. इसका उपयोग सक्षम करने के लिए, इसे सक्षम करें के रूप में चिह्नित करें।",
        "enable_replace": "मॉडल का उपयोग सक्षम करने के लिए इसे चेक करें।",
        "sec2_title": "### 2. प्रत्येक संबंधित बोलने वाले के प्रत्येक TTS को लागू करने के लिए एक आवाज़ का चयन करें और विन्यास लागू करें।",
        "sec2_subtitle": "आपके पास कितने <TTS बोलने वाले> हैं, इस पर निर्भर करता है, प्रत्येक को उसका संबंधित मॉडल चाहिए। विशेषज्ञ नहीं पाया गया है।",
        "cv_tts1": "बोलने वाले 1 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts2": "बोलने वाले 2 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts3": "बोलने वाले 3 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts4": "बोलने वाले 4 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts5": "बोलने वाले 5 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts6": "बोलने वाले 6 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts7": "बोलने वाले 7 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts8": "बोलने वाले 8 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts9": "बोलने वाले 9 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts10": "बोलने वाले 10 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts11": "बोलने वाले 11 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts12": "बोलने वाले 12 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_aux": "- यदि किसी कारणवश स्पीकर सही ढंग से पहचाना नहीं गया है, तो लागू करने के लिए आवाज़।",
        "cv_button_apply": "आवेदन को लागू करें",
        "tab_help": "सहायता",
    },
    
    "marathi": {
        "description": """
        ### 🎥 **Vit च्या विद्यार्थाद्वारे केला गेलेला एक प्रोजेक्ट ** 📽️

        एक व्हिडिओ, ऑडिओ फाईल अपलोड करा किंवा एक YouTube लिंक प्रदान करा. 📽️ **अद्यतनित नोटबुक घ्या आधिकृत भंडारात।: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        तपशील देखण्यासाठी 'मदत' टॅब पहा. व्हिडिओ अनुवादासोबत मजा करण्याची सुरवात करूया! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **वापरायला निर्देशिका:**

        1. 📤 **व्हिडिओ**, **ऑडिओ फाईल** अपलोड करा किंवा 🌐 **YouTube लिंक प्रदान करा.**

        2. 🌍 व्हिडिओ **अनुवाद** करण्यासाठी कोणत्या **भाषेत निवडा.**

        3. 🗣️ व्हिडिओमध्ये **किती लोक बोलत आहेत** ते स्पष्ट करा आणि प्रत्येकाला अनुवाद भाषेसाठी उपयुक्त TTS द्या.

        4. 🚀 '**अनुवाद**' बटण दाबा निकाल मिळवण्यासाठी.

        ---

        # 🧩 **SoniTranslate विविध TTS (पाठ-टू-स्पीच) इंजिनसाठी समर्थन करते, ज्या म्हणजे:**
        - EDGE-TTS → स्वरूप `en-AU-WilliamNeural-Male` → जलद आणि खात्रीशील.
        - FACEBOOK MMS → स्वरूप `en-facebook-mms VITS` → ध्वनी अधिक प्राकृतिक आहे; ह्या क्षणी, हे केवळ CPU वापरते.
        - PIPER TTS → स्वरूप `en_US-lessac-high VITS-onnx` → म्हणजे अखेरचा, परंतु ह्यात CPU आणि GPU दोन्हीत अनुकूलित केले आहे.
        - BARK → स्वरूप `en_speaker_0-Male BARK` → चांगली गुणवत्ता परंतु मंद, आणि हे हल्ल्यांसाठी आदर्श आहे.
        - OpenAI TTS → स्वरूप `>alloy OpenAI-TTS` → बहुभाषिक आहे पण OpenAI API की आवश्यकता आहे
        - Coqui XTTS → स्वरूप `_XTTS_/AUTOMATIC.wav` → केवळ उपलब्ध आहे: चिनी (सरलीकृत), इंग्रजी, फ्रेंच, जर्मन, इटालियन, पोर्तुगीज, पोलिश, तुर्की, रशियन, डच, चेक, अरबी, स्पॅनिश, हंगेरियन, कोरियन आणि जपानी.

        ---

        # 🎤 कसे वापरावे आर.व्ही.सी. आणि आर.व्ही.सी.2 आवाज (पर्वतीय) 🎶

        उद्दिष्ट म्हणजे उत्पन्न केलेल्या TTS (पाठ-टू-स्पीच) वर एक आर.व्ही.सी. लागू करा 🎙️

        1. `कस्टम व्हॉईस आर.व्ही.सी.` टॅबमध्ये, आपल्याला आवश्यक असलेल्या मॉडेल्स डाउनलोड करा 📥 आपण Hugging Face आणि Google Drive यांच्या लिंक्सचा वापर करू शकता, जसे की zip, pth किंवा इंडेक्स. आपण पूर्ण HF स्पेस भंडारांचा डाउनलोड करू शकता, परंतु ह्या पर्यायाचा स्थिरपणा काही कमी आहे 😕

        2. आता, `आर.व्ही.सी. च्या आवाजाच्या TTS ला बदला: टीटीएस ते आर.व्ही.सी.` आणि `सक्षम` बॉक्स तपासा ✅ यानंतर, आपण प्रत्येक TTS वक्त्याला लागणारा मॉडेल निवडू शकता 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. सर्व आर.व्ही.सी. ला लागू केलेला F0 विधान अनुकूलीत करा 🎛️

        4. आपल्याने केलेल्या बदल लागू करण्यासाठी `अनुप्रयोग बदल` दाबा 🔄

        5. व्हिडिओ अनुवाद टॅबमध्ये परत जा आणि 'अनुवाद' वर क्लिक करा ▶️ आता, अनुवाद R.V.C. लागू करत आहे 🗣️

        सूचना: आपण `टेस्ट आर.व्ही.सी.` वापरू शकता व सर्वोत्तम TTS किंवा आर.व्ही.सी. लागू करण्यासाठी गुणवत्ता शोधण्यासाठी वापरू शकता 🧪🔍

        ---

        """,
        "tab_translate": "व्हिडिओ अनुवाद",
        "video_source": "व्हिडिओ स्रोत निवडा",
        "link_label": "मीडिया लिंक.",
        "link_info": "उदाहरण: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL येथे जातो...",
        "dir_label": "व्हिडिओ मार्ग.",
        "dir_info": "उदाहरण: /usr/home/my_video.mp4",
        "dir_ph": "मार्ग येथे जातो...",
        "sl_label": "मूळ भाषा",
        "sl_info": "हे व्हिडिओची मूळ भाषा आहे",
        "tat_label": "ऑडिओ अनुवाद करा",
        "tat_info": "लक्ष्य भाषा निवडा आणि त्या भाषेसाठी संबद्ध TTS निवडण्यास सुनिश्चित करा.",
        "num_speakers": "व्हिडिओमध्ये किती लोक बोलत आहेत हे निवडा.",
        "min_sk": "किमान बोलताही",
        "max_sk": "किमान बोलताही",
        "tts_select": "प्रत्येक वक्त्यासाठी आपल्याला कसा आवाज आवडतो ते निवडा.",
        "sk1": "TTS वक्त्य 1",
        "sk2": "TTS वक्त्य 2",
        "sk3": "TTS वक्त्य 3",
        "sk4": "TTS वक्त्य 4",
        "sk5": "TTS वक्त्य 5",
        "sk6": "TTS वक्त्य 6",
        "sk7": "TTS वक्त्य 7",
        "sk8": "TTS वक्त्य 8",
        "sk9": "TTS वक्त्य 9",
        "sk10": "TTS वक्त्य 10",
        "sk11": "TTS वक्त्य 11",
        "sk12": "TTS वक्त्य 12",
        "vc_title": "विविध भाषांमध्ये आवाज नक्कल",
        "vc_subtitle": """
        ### विविध भाषांमध्ये व्यक्तीचा आवाज पुनर्निर्मित करा.
        अनुकूलप्रद केल्यास अधिकांश आवाजांसह अद्याप अव्याप्ती न मिळताना, प्रत्येक गोष्टीत उपयोगी आहे. आवाज पुनर्निर्मित केवळ संदर्भ वक्त्याच्या टोन अधिल्यास आहे, ज्याची मूळ वक्त्य TTS मॉडेल द्वारे नियंत्रित केली जाते आणि नक्कल करणारी नाही. या विधानाने एका प्रमुख व्हिडिओतील प्रत्येक वक्त्याचे ऑडियो संच घेऊन ते प्रक्रिया करेल.
        """,
        "vc_active_label": "सक्रिय आवाज नक्कल",
        "vc_active_info": "सक्रिय आवाज नक्कल: मूळ वक्त्याचा आवाज पुनर्निर्मित करते",
        "vc_method_label": "पद्धत",
        "vc_method_info": "आवाज नक्कल प्रक्रियेसाठी एक पद्धत निवडा",
        "vc_segments_label": "कमाल सॅम्पल्स",
        "vc_segments_info": "कमाल सॅम्पल्स: प्रक्रियेसाठी ऑडियो सॅम्पल्सची संख्या आहे, अधिक चांगलं आहे परंतु ते आवाज जोडणारं करू शकतात",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: ऑडियो सॅम्पल्सवर ध्वनीक सांकेतिक दिवस लागू करते.",
        "vc_remove_label": "आधीचे सॅम्पल्स काढा",
        "vc_remove_info": "आधीचे सॅम्पल्स काढा: मागील सॅम्पल्स काढा: मागील सॅम्पल्स काढा, म्हणजे नवीन सामग्री करण्यासाठी त्या नवीन सॅम्पल्स बनवणे आवश्यक आहे.",
        "xtts_title": "ऑडियोवर आधारित TTS तयार करा",
        "xtts_subtitle": "आवाजासह 10 सेकंदांचा मोठा ऑडियो फाईल अपलोड करा. XTTS वापरून, दिलेल्या ऑडियो फाईलसोबत समान आवाजासह नवीन TTS तयार केला जाईल.",
        "xtts_file_label": "आवाजासह एक क्षिप्र ऑडियो अपलोड करा",
        "xtts_name_label": "TTS साठी नाव",
        "xtts_name_info": "एक साधा नाव वापरा",
        "xtts_dereverb_label": "ऑडियोवर ध्वनीक सांकेतिक दिवस लागू करा",
        "xtts_dereverb_info": "ऑडियोवर ध्वनीक सांकेतिक दिवस लागू करा: ऑडियोवर ध्वनीक सांकेतिक दिवस लागू करते",
        "xtts_button": "ऑडियो प्रक्रिया करा आणि त्यामध्ये समाविष्ट करा",
        "xtts_footer": "स्वयंचली आवाज XTTS उत्पादित करा: आपण TTS निवडकासाठी `_XTTS_/AUTOMATIC.wav` वापरू शकता, प्रत्येक वक्त्यासाठी नवीन सेगमेंट उत्पन्न करण्यासाठी आणि अनुवाद वापरताना एकत्रित करण्यासाठी।",
        "extra_setting": "उन्नत सेटिंग्ज",
        "acc_max_label": "ऑडियो अधिकतम एक्सेलरेशन",
        "acc_max_info": "ओव्हरलॅपिंग टाळण्यासाठी अनुवादित ऑडियो सेगमेंटसाठी अधिकतम एक्सेलरेशन. 1.0 ची एक मूल्य अधिकतम एक्सेलरेशन प्रतिनिधित्व करते",
        "acc_rate_label": "वेगवर्धी दर व्यवस्थापन",
        "acc_rate_info": "वेगवर्धी दर व्यवस्थापन: अल्प गतीचे आवश्यक असलेले क्षेत्र समायोजित करण्यासाठी वेगवर्धी व्यवस्थापन करते, सततता ठेवते आणि पुढील सुरुवातीचा वेळ मलान घेतला जातो.",
        "or_label": "ओव्हरलॅप कमी करा",
        "or_info": "ओव्हरलॅप कमी करा: मागील समाप्तीच्या वेळेस आधारित सुरुवातीच्या वेळा समायोजित करून सेगमेंट ओव्हरलॅप होण्यास रोखते; समकालिकरण अडचणी उत्पन्न करू शकतो.",
        "aud_mix_label": "ऑडियो मिक्सिंग पद्धत",
        "aud_mix_info": "स्वच्छ आणि संतुलित आउटपुट सादर करण्यासाठी मूळ आणि अनुवादित ऑडियो फाईल्स एकत्रित करण्यासाठी आवश्यक दोन मिक्सिंग मोड्युल्या सोडल्या आहेत.",
        "vol_ori": "मूळ ऑडियोची व्हॉल्यूम",
        "vol_tra": "अनुवादित ऑडियोची व्हॉल्यूम",
        "voiceless_tk_label": "आवाजरहित ट्रॅक",
        "voiceless_tk_info": "आवाजरहित ट्रॅक: अनुवादित ऑडियोसोबत संयुक्त करण्यापूर्वी मूळ ऑडियोची आवाजे काढा.",
        "sub_type": "उपशीर्षक प्रकार",
        "soft_subs_label": "कोमल सबटायटल्स",
        "soft_subs_info": "कोमल सबटायटल्स: दर्शक व्हिडिओ पाहताना चालू निशांत करू शकतात किंवा बंद करू शकतात.",
        "burn_subs_label": "सबटायटल्स जळवा",
        "burn_subs_info": "सबटायटल्स जळवा: व्हिडिओमध्ये सबटायटल्स आजार करा, त्यांना दृश्यांतराचा कोणताही स्थायी भाग बनवून करा.",
        "whisper_title": "वाचन विक्रमण संरचना.",
        "lnum_label": "संख्या शब्दांतर",
        "lnum_info": "संख्या शब्दांतर: अंकांचे प्रतिनिधित्व लेखित सर्वकाशांमध्ये बदला करा.",
        "scle_label": "आवाज स्वच्छता",
        "scle_info": "आवाज स्वच्छता: वादला तयार करण्यापूर्वी आवाज आणि बॅकग्राऊंड ध्वनी काढा. हे काम वेगवेगळ्या आवाज फाईल्ससह करता येऊ शकते.",
        "sd_limit_label": "सेगमेंट अवधी सीमा",
        "sd_limit_info": "प्रत्येक सेगमेंटसाठी कोणत्याही अवधीचा महासूचीत (सेकंदांमध्ये) सुनिश्चित करा. ऑडिओ वाडचा वापर करून प्रत्येक सेगमेंटच्या तुकड्याची अवधी सीमित करण्यात येईल.",
        "asr_model_info": "जीवनाचा मूळ 'फिस्फिंग' मॉडेल वापरून बोललेली भाषा ते टेक्स्टमध्ये बदलते. उदाहरणार्थ, चीनी भाषेतील फायनट्यून्ड मॉडेल वापरण्यासाठी ड्रॉपडाऊनमध्ये 'BELLE-2/Belle-whisper-large-v3-zh' संग्रह नाव नोंदवा. Hugging Face वर फायनट्यून्ड मॉडेल्स शोधा.",
        "ctype_label": "गणना प्रकार",
        "ctype_info": "int8 किंवा float16 आढळवून कमी डेटा प्रकारांमध्ये निर्देशन करणे कामाची वेगवेगळी प्रदर्शन करू शकते आणि गणना द्वारे अपेक्षित क्षमतेची वाढवू शकते, परंतु float32 आणि इतर मोठ्या डेटा प्रकारांपेक्षा निश्चितता कुठल्या प्रकारे कमी करू शकते.",
        "batchz_label": "बॅच आकार",
        "batchz_info": "आपल्याला कमी VRAM असलेले GPU असल्यास बॅच आकार कमी करणे मेमरी झटका आणू शकते आणि मेमरी नसलेली समस्या व्यवस्थापित करण्यास मदत करू शकते.",
        "tsscale_label": "टेक्स्ट सेगमेंटेशन पैमाना",
        "tsscale_info": "पाठाचे सेगमेंट वाक्य, शब्द किंवा अक्षरांमध्ये वागवा. शब्द आणि अक्षर सेगमेंटेशन उपशीर्षकसाठी उपयुक्त तंत्रज्ञान उपलब्ध करून देतात; अनुवाद बंद करणे मूल संरचना संरक्षित करते.",
        "srt_file_label": "एसआरटी उपशीर्षक फाईल अपलोड करा (व्हिस्परच्या विवेचनाच्या विरोधात वापरली जाईल)",
        "divide_text_label": "टेक्स्ट सेगमेंट्स पुनर्विभाजित करा:",
        "divide_text_info": "(प्रयोगशील) स्रोत भाषेतील विद्यमान टेक्स्ट सेगमेंट्सचा विभाग करण्यासाठी एक विभाजक प्रविष्ट करा. टूलला उपलब्धींना ओळखण्यासाठी आणि नुकसानकर्ता करण्यासाठी त्यामुळे नवीन सेगमेंट्स निर्मित करते. | चा वापर करून अनेक विभाजक स्पष्ट करा, उदा.: !|?|...|।",
        "diarization_label": "डायरिझेशन मॉडेल",
        "tr_process_label": "भाषांतर प्रक्रिया",
        "out_type_label": "आउटपुट प्रकार",
        "out_name_label": "फाईलचं नाव",
        "out_name_info": "आउटपुट फाईलचं नाव",
        "task_sound_label": "काम स्थिती आवाज",
        "task_sound_info": "काम स्थिती आवाज: काम संपल्याचे किंवा क्रियाकलापातील त्रुटी दर्शवणारा ध्वन आवाज करा.",
        "cache_label": "प्रगती पुनर्प्राप्त करा",
        "cache_info": "प्रगती पुनर्प्राप्त करा: शेवटचा चेकपॉईंट येथून प्रक्रिया सुरू करा.",
        "preview_info": "परीक्षणासाठी व्हिडिओला केवळ 10 सेकंदांसाठी कट्टा करते. कृपया पूर्ण व्हिडिओ अवधी प्राप्त करण्यासाठी हे निष्क्रिय करा.",
        "edit_sub_label": "तयार केलेले उपशीर्षक संपादित करा",
        "edit_sub_info": "तयार केलेले उपशीर्षक संपादित करा: अनुवाद करण्यासाठी 2 चरणांमध्ये अनुवाद चालवण्याची परवानगी देते. पहिल्यांदा 'उपशीर्षक मिळवा आणि संपादित करा' बटणावर क्लिक करून तुम्हाला उपशीर्षक मिळेल आणि त्या संपादित करण्यासाठी, आणि त्यानंतर 'अनुवाद' बटणावर क्लिक करून, आपण व्हिडिओ तयार करू शकता",
        "button_subs": "उपशीर्षक मिळवा आणि संपादित करा",
        "editor_sub_label": "तयार केलेले उपशीर्षक",
        "editor_sub_info": "येथील तयार केलेल्या उपशीर्षकांमध्ये टेक्स्ट संपादित करण्यासाठी मनःपूर्वक वापरा. आपण 'अनुवाद' बटणावर क्लिक करण्यापूर्वी, संवादीचे निवडणे, 'मूळ भाषा', 'ऑडियोचे अनुवाद करा', आणि 'अधिक स्पीकर्स' या अनुक्रमात किंवा संरचना विकल्प बदलू शकता, त्यांचा अशा चुकांवर टाकण्यासाठी. एकदा तुम्ही संपू नेल, 'अनुवाद' बटणावर क्लिक करा.",
        "editor_sub_ph": "प्रथम 'उपशीर्षक मिळवा आणि संपादित करा' बटणावर क्लिक करण्यात येतो",
        "button_translate": "अनुवाद करा",
        "output_result_label": "अनुवादित व्हिडिओ डाउनलोड करा",
        "sub_ori": "उपशीर्षक",
        "sub_tra": "अनुवादित उपशीर्षक",
        "ht_token_info": "एक महत्त्वाचं कार्य म्हणजे Pyannote वापरासाठी लायसेंस समजून घेणे. आपल्याला Hugging Face वर एक खाते असावी लागते आणि मॉडेल्स वापरण्यासाठी लायसेंस स्वीकारा लागते: https://huggingface.co/pyannote/speaker-diarization आणि https://huggingface.co/pyannote/segmentation. आपल्याला येथे आपला की टोकन मिळेल: https://hf.co/settings/tokens",
        "ht_token_ph": "टोकन येथे जाते...",
        "tab_docs": "कागदपत्र अनुवाद",
        "docs_input_label": "कागदपत्र स्रोत निवडा",
        "docs_input_info": "ते पीडीएफ, डॉक्स, टीएक्सट किंवा मजकूर होऊ शकते",
        "docs_source_info": "हे मजकूरची मूळ भाषा आहे",
        "chunk_size_label": "प्रत्येक सेगमेंट प्रत्येक करकटाने TTS ला प्रक्रिया करण्यासाठी अधिकतम अक्षरांची संख्या",
        "chunk_size_info": "0 चा मूल्य एक विनामूल्य आणि अधिक संगणकांसाठी संगणकात अधिक संगणकांसाठी अनुकूलित मूल्य नेमल्याची अर्थी होतो.",
        "docs_button": "भाषा कन्वर्ट ब्रिज सुरू करा",
        "cv_url_info": "यूआरएलपासून ऑटोमॅटिक रॉकी मॉडेल्स डाउनलोड करा. तुम्ही HuggingFace किंवा Drive ची लिंक वापरू शकता, आणि तुम्हाला किंवा तुम्हाला प्रत्येक लिंक, प्रत्येक लिंक समाविष्ट करण्यासाठी प्रत्येक लिंक वापरू शकता, प्रत्येक लिंक वापरू शकता. उदाहरण: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "आवाज बदला: TTS ते R.V.C.",
        "sec1_title": "### 1. त्याचा वापर सक्षम करण्यासाठी, ते सक्षम जाहीर करा.",
        "enable_replace": "मॉडेल्सचा वापर सक्षम करण्यासाठी हे तपासा.",
        "sec2_title": "### 2. प्रत्येक TTS च्या प्रत्येक प्रतिनिधीत्व करण्यासाठी आवाज निवडा आणि सेटिंग्ज लागू करा.",
        "sec2_subtitle": "आपण किती <TTS Speaker> वापरणार आहात यानुसार, प्रत्येकाने स्वत: च्या मॉडेलची आवश्यकता आहे. अधिक केल्यासाठी, अधिक स्पेकरच्या उपयोगासाठी एक सहाय्यक असते जर कारणाने वक्ता सही रिकामे ओळखले जात नाहीत.",
        "cv_tts1": "स्पीकर 1 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts2": "स्पीकर 2 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts3": "स्पीकर 3 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts4": "स्पीकर 4 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts5": "स्पीकर 5 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts6": "स्पीकर 6 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts7": "स्पीकर 7 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts8": "स्पीकर 8 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts9": "स्पीकर 9 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts10": "स्पीकर 10 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts11": "स्पीकर 11 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts12": "स्पीकर 12 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_aux": "- जर कारणाने वक्ता सही ओळखले जात नाही तर लागू करण्यासाठी आवाज.",
        "cv_button_apply": "सेटिंग्ज लागू करा",
        "tab_help": "मदत",
    },
}
