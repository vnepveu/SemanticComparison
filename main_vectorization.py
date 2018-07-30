import main_text_treatment
import text_2_vec
import document_io
import main_model

vector_file_name = main_text_treatment.save_name + '_vectorized_without_subject'
if __name__ == "__main__":
    model = text_2_vec.load_model(main_model.model_name)
    file = document_io.load(main_model.save_name, "text_processed")
    for string in []:
        file.pop(string)
    key_list = []
    value_list = []
    for key, value in file.items():
        key_list.append(key)
        value_list.append(value)
    text_2_vec.save_to_memory(key_list=key_list, value_list=value_list, filename=vector_file_name, w2v_model=model)
