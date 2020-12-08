import { React } from 'react';
import { Card, Form, Button, Row, Col } from 'react-bootstrap'

const FormMain = () => {

    async function handleSubmit(e) {
        e.preventDefault()
        console.log('Submitted')
    }

    return (
        <>

                    <h2 className="text-center mb-4">Main Form</h2>
                    <Form onSubmit={handleSubmit}>


                        <Form.Group controlId="formProjectTitle">
                            <Form.Label><b>Project Title</b></Form.Label>
                            <Form.Control type="text" required />
                        </Form.Group>


                        <Form.Group>
                            <Form.Label>
                                <b>Where will the study activities take place? Please be sure to select all program areas that the participant recruitment and study visits will take place.</b>
                            </Form.Label>
                        
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
                        </Form.Group>

                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                    </Form>

        </>
    )
}

export default FormMain