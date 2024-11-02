# Use the official AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Set the environment variable to specify where to look for modules
ENV PYTHONPATH=/var/task/src

# Copy application code to the /var/task/src directory (where Lambda will look)
COPY src/ /var/task/src/

# Copy layer-specific requirements.txt to install Lambda dependencies
COPY layer/requirements.txt /var/task/layer_requirements.txt

# Install dependencies for Lambda execution, targeting /var/task (Lambda’s default code directory)
RUN pip install -r /var/task/layer_requirements.txt --target /var/task/

# Set the command to run the Lambda handler
CMD ["src.app.lambda_handler"]
