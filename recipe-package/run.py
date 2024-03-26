from recipe import pipeline

if __name__ == "__main__":
    # Assuming `pipeline` is a function that returns an Apache Beam pipeline
    p = pipeline()
    # Run the pipeline using the DirectRunner
    result = p.run()
    result.wait_until_finish()
