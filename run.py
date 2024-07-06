import cv2

list_of_names = []

def cleanup_data():
    with open("name-list-data.txt") as file:
        for line in file:
            list_of_names.append(line.strip())

def generate_certificates():
    for index, name in enumerate(list_of_names):
        template = cv2.imread("certificate-template.jpg")
        cv2.putText(template, name, (815, 1500), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 5, cv2.LINE_AA)
        cv2.imwrite(f'generated-certificated-data/{name}.jpg', template)
        print(f'Processing {index + 1} / {len(list_of_names)}')

cleanup_data()
generate_certificates()