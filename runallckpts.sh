while IFS= read -r filename; do
    # file="logs/exp1/$filename"
    file=$filename

    # Append formatted text to logs.log
    echo -e "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n$file\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" >> logs/exp1/logs.log

    # Print the filename
    echo ":::::::::::::::RUNNING $file:::::::::::::::"

    # Run the Python script with the current file
    python procedure_learning_eval.py --cfg configs/PC_Disassembly_config.yaml TCC.MODEL_PATH "$file"
done < runtheseckpts.txt
