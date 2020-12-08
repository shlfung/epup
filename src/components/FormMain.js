import { React } from 'react';
import { Form, Button, Row, Col } from 'react-bootstrap'

const FormMain = () => {
    return (
        <div>
            <Form>
                <Form.Group controlId="formProjectTitle">
                    <Form.Label>Project Title</Form.Label>
                </Form.Group>


                <Form.Group as={Row}>
                    <Form.Label as="legend" column sm={2}>
                        Where will the study activities take place? Please be sure to select all program areas that the participant recruitment and study visits will take place.
                    </Form.Label>
                    <Col sm={10}>
                        <Form.Check
                            type="checkbox"
                            label="Health Information Management"
                            name="formHorizontalRadios"
                            id="formHorizontalRadios1"
                        />
                        <Form.Check
                            type="checkbox"
                            label="Emergency Medicine"
                            name="formHorizontalRadios"
                            id="formHorizontalRadios2"
                        />
                        <Form.Check
                            type="checkbox"
                            label="Medical Day Unit"
                            name="formHorizontalRadios"
                            id="formHorizontalRadios3"
                        />
                    </Col>
                </Form.Group>

                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </div>
    )
}

export default FormMain