# Use a Node.js runtime as a parent image
FROM node:20-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./

# Install any needed packages specified in package.json
RUN npm install

# Copy the rest of the application's code to the working directory
COPY . .

# Expose port 3000 to the outside world
EXPOSE 3000

# Command to run the application in development mode
CMD ["npm", "run", "dev"]
